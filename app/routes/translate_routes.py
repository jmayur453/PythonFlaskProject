from flask import Blueprint, request, jsonify
from app.utils.translator import translate_text

translate_api = Blueprint('translate_api', __name__)
@translate_api.route('/translate', methods=['POST'])
def handle_translation():
    data = request.get_json()
    text = data.get('text', '')
    lang = data.get('lang', 'hi')

    if not text:
        return jsonify({'success': False, 'message': 'Text is required'}), 400

    try:
        translated = translate_text(text, dest_lang=lang)
        return jsonify({'success': True, 'translated_text': translated})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
