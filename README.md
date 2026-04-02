# PyBot — AI Chatbot 🤖

![Live](https://img.shields.io/badge/Live-Online-brightgreen)
![React](https://img.shields.io/badge/React-Frontend-blue)
![Python](https://img.shields.io/badge/Python-Backend-yellow)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green)
![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3-orange)
![Netlify](https://img.shields.io/badge/Deployed-Netlify-teal)

I built this chatbot as part of my AI/ML learning journey.
It started as a simple rule-based bot and grew into a
full-stack AI-powered application.

🔗 **Try it live:** https://pybot-chatbot.netlify.app

---

## What does it do?

You can chat with it like ChatGPT. It understands English,
Punjabi, Hindi and German. You can also use your voice
to talk to it instead of typing.

---

## Features I built

- Real-time AI responses that stream word by word
- Voice input with live sound wave animation
- Chat history that saves even after you close the browser
- Multiple chat sessions like ChatGPT sidebar
- Works on mobile and desktop
- Supports English, ਪੰਜਾਬੀ, हिंदी and Deutsch

---

## Tech I used

| Layer | Technology |
|-------|-----------|
| Frontend | React.js |
| Backend | Python + Flask |
| Database | MongoDB Atlas |
| AI Model | Groq LLaMA 3.3 70B |
| Deployment | Netlify + Render |

---

## How to run it yourself
```bash
# Clone the project
git clone https://github.com/Anmol040/pybot-chatbot.git
cd pybot-chatbot

# Setup Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Add your keys in .env file
GROQ_API_KEY=your_key_here
MONGO_URI=your_mongodb_uri_here

# Start the backend
python server.py

# In a new terminal start the frontend
cd frontend
npm install
npm start
```

---

## Project structure
```
pybot-chatbot/
├── server.py        → Flask backend + API routes
├── chatbot.py       → Simple terminal chatbot
├── intents.py       → Basic Q&A intents
├── requirements.txt → Python packages
└── frontend/
    └── src/
        └── App.js   → Full React UI
```

---

## What I learned

Building this taught me how to connect a React frontend
to a Python backend, work with MongoDB, use AI APIs,
and deploy a full-stack app for free.

Still improving it — next up is user authentication.

---

Built by **Anmol Bhardwaj** 👨‍💻
📍 Currently studying in Germany
