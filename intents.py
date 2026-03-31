# intents.py
# All Questions and Answers for Bot
# ਬੋਟ ਦੇ ਸਾਰੇ ਸਵਾਲ ਅਤੇ ਜਵਾਬ

intents = {

    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "responses": [
            "Hello! How are you? 😊",
            "Hey! I am PyBot 🤖"
        ]
    },

    "how_are_you": {
        "patterns": ["how are you", "how r u"],
        "responses": [
            "I am great! Thanks 😄",
            "Doing awesome! 🤖"
        ]
    },

    "bye": {
        "patterns": ["bye", "goodbye"],
        "responses": [
            "Goodbye! 👋",
            "Bye! Come back soon 😊"
        ]
    },

}