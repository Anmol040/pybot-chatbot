# chatbot.py
# AI Powered PyBot using Groq
# Groq ਨਾਲ AI PyBot

import os
from groq import Groq
from dotenv import load_dotenv

# Load API Key from .env file
# .env ਫ਼ਾਈਲ ਤੋਂ API Key ਲਓ
load_dotenv()

# Connect to Groq AI
# Groq AI ਨਾਲ ਜੋੜੋ
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Chat history — remembers conversation
# ਗੱਲਬਾਤ ਯਾਦ ਰੱਖਦਾ ਹੈ
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Answer in the same language the user speaks. If they write in Punjabi, reply in Punjabi. If Hindi, reply in Hindi. If German, reply in German. If English, reply in English."
    }
]

# Run the bot
print("=" * 45)
print("🤖 AI PyBot is ready!")
print("   ਤੁਹਾਡਾ AI PyBot ਤਿਆਰ ਹੈ!")
print("   Type 'bye' to exit")
print("=" * 45)

while True:
    # Get user input
    user = input("\nYou 👤 : ")

    # Check if empty
    if user.strip() == "":
        continue

    # Check if bye
    if "bye" in user.lower():
        print("PyBot 🤖 : Goodbye! 👋")
        break

    # Add user message to history
    messages.append({
        "role": "user",
        "content": user
    })

    # Send to Groq AI and get reply
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    # Get the reply
    reply = response.choices[0].message.content

    # Save reply to history
    messages.append({
        "role": "assistant",
        "content": reply
    })

    # Show reply
    print("PyBot 🤖 :", reply)