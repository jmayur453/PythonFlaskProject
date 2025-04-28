from flask import Blueprint, request, jsonify
from app.utils.openai_chatbot import get_gemini_response

chatbot_api = Blueprint("chatbot_api", __name__)

@chatbot_api.route("/chatbot", methods=["POST"])
def chatbot_reply():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"success": False, "message": "Message required"}), 400

    reply = get_gemini_response(message)
    return jsonify({"success": True, "reply": reply})
