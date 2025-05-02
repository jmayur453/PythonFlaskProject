from flask import Blueprint, request, jsonify
from app.utils.youtube_downloader import download_video_from_url

youtube_api = Blueprint('youtube_api', __name__)

@youtube_api.route('/download', methods=['POST'])
def handle_youtube_download():
    data = request.get_json()
    url = data.get('url', '').strip()

    if not url:
        return jsonify({'success': False, 'message': 'YouTube URL is required'}), 400

    try:
        result = download_video_from_url(url)
        if result['success']:
            return jsonify({'success': True, 'message': result['message'], 'output_dir': result['output_dir']})
        else:
            return jsonify({'success': False, 'message': result['message']}), 500
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

