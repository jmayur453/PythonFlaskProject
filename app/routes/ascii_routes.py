from flask import Blueprint, request, jsonify
from app.utils.ascii_art_generator import image_to_ascii

ascii_bp = Blueprint('ascii', __name__)

@ascii_bp.route('/ascii-art', methods=['POST'])
def ascii_art():
    if 'image' not in request.files:
        return jsonify({'success': False, 'message': 'No image uploaded'}), 400

    image = request.files['image']

    try:
        ascii_art = image_to_ascii(image)
        return jsonify({'success': True, 'ascii': ascii_art})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
