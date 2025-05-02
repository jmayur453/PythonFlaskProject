import os
import subprocess

def download_video_from_url(url):
    try:
        output_dir = os.path.join(os.getcwd(), "ClippedVideos")
        os.makedirs(output_dir, exist_ok=True)

        command = [
            os.path.join(os.path.dirname(__file__), 'yt-dlp.exe'),
            #"--cookies-from-browser", "chrome",  # Only needed for Instagram/Private content
            "-o", os.path.join(output_dir, "%(title)s.%(ext)s"),
            url
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            return {
                'success': True,
                'message': 'Download completed successfully.',
                'output_dir': output_dir
            }
        else:
            return {
                'success': False,
                'message': f'yt-dlp error: {result.stderr.strip()}'
            }

    except Exception as e:
        return {
            'success': False,
            'message': f'Exception occurred: {str(e)}'
        }
