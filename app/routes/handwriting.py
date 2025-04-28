from flask import Blueprint, request, jsonify, send_file
from app.utils.handwriting_generator import generate_handwriting_image
import os

handwriting_bp = Blueprint('generate-handwriting', __name__)
@handwriting_bp.route('/generate-handwriting', methods=['POST'])
def handwriting():
    data = request.get_json()
    text = data.get('text')
    font = data.get('font', 'handwriting.ttf')  # default font

    if not text:
        return jsonify({'success': False, 'message': 'Text is required'}), 400

    try:
        img_path = generate_handwriting_image(text, font)
        return send_file(img_path, mimetype='image/png')
    except Exception as e:
        print(f"Error: {str(e)}")  # Log the error to console
        return jsonify({'success': False, 'message': str(e)}), 500
