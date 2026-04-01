# server.py
# PyBot Backend with MongoDB

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to Groq AI
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Connect to MongoDB
import certifi
mongo = MongoClient(os.environ.get("MONGO_URI"), tlsCAFile=certifi.where())
db = mongo["pybot"]
chats_collection = db["chats"]

system_prompt = """You are PyBot, a friendly AI assistant made by Mr Bhardwaj.
Always reply in a simple, easy, and human-like way.
Use short sentences. Use examples. Be friendly and warm.
Format answers clearly with bullet points when needed.
Reply in the same language the user uses.
Never sound robotic. Sound like a helpful friend."""

@app.route("/chats", methods=["GET"])
def get_chats():
    chats = list(chats_collection.find(
        {}, 
        {"_id": 0}
    ).sort("created_at", -1))@app.route("/chats", methods=["GET"])
def get_chats():
    user_id = request.args.get("userId", "default")
    chats = list(chats_collection.find(
        {"user_id": user_id}, 
        {"_id": 0}
    ).sort("created_at", -1))
    return jsonify(chats)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    chat_id = data.get("chatId")
    user_message = data.get("message")

    # Find existing chat
    user_id = data.get("userId", "default")
    chat = chats_collection.find_one({"chat_id": chat_id})

    user_id = data.get("userId", "default")
    if not chat:
        chat = {
            "chat_id": chat_id,
            "user_id": user_id,
            "title": user_message[:30],
            "created_at": datetime.now(),
            "messages": [
                {"role": "system", "content": system_prompt}
            ]
        }

    # Add user message
    chat["messages"].append({
        "role": "user",
        "content": user_message
    })

    # Get AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=chat["messages"]
    )

    reply = response.choices[0].message.content

    # Add bot reply
    chat["messages"].append({
        "role": "assistant",
        "content": reply
    })

    # Save to MongoDB
    chats_collection.update_one(
        {"chat_id": chat_id},
        {"$set": chat},
        upsert=True
    )

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=8001, debug=True)