from flask import Blueprint, request, send_file
from app.utils.image_editor import edit_uploaded_image

image_api = Blueprint('image_api', __name__)

@image_api.route('/edit-image', methods=['POST'])
def edit_image():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    file = request.files['image']
    edited_image = edit_uploaded_image(file)
    return send_file(edited_image, mimetype='image/png')
