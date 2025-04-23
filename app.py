from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv # type: ignore
import google.generativeai as genai # type: ignore
import os

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')

genai.configure(api_key="AIzaSyAx3GvlgvMnhs9zjM6a5-bKleD6Aa2_QYY")
model = genai.GenerativeModel("gemini-1.5-flash")
chat_session = model.start_chat(history=[
    {
    "role": "user",
    "parts": [
        "You are a concise and friendly AI financial advisor. Follow these rules:",
        
        "1. Keep responses SHORT and FOCUSED - max 2-3 sentences per point",
        "2. Use bullet points for multiple items",
        "3. Always start with a brief greeting/acknowledgment",
        "4. Break complex topics into simple steps",
        "5. Use emojis to make points clear: 💵 money, 📈 investments, 🏦 savings, 💳 credit, 🎯 goals",
        
        "Response Format:",
        "- Brief greeting",
        "- 2-3 key points maximum",
        "- One clear action step",
        
        "Example Response:",
        "Hi! Here's what you need to know about budgeting:",
        "• Track income and expenses 📊",
        "• Set aside 20% for savings 🏦",
        "Next step: Start by noting all expenses for one week 📝",
        
        "Remember:",
        "- No long paragraphs",
        "- Focus on actionable advice",
        "- Keep it simple and clear",
        "- Always end with a next step"
    ]
    }
])

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        response = chat_session.send_message(user_input)
        # Clean up the response text, remove unnecessary markdown characters
        clean_response = response.text.replace("**", "").replace("*", "")
        return jsonify({"reply": clean_response if clean_response else "I'm here to help with your financial questions!"})
    except Exception as e:
        return jsonify({"reply": f"Gemini API Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)