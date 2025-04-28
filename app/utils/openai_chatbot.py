import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def get_gemini_response(message: str):
    if not API_KEY:
        return "❌ Missing API key in .env file."

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": message}
                ]
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "❌ Error parsing response."
    else:
        return f"❌ Error: {response.status_code} - {response.text}"
