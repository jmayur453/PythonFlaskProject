from flask import Blueprint, jsonify
from app.utils.geolocation_tracker import get_location_map

geolocation_api = Blueprint('geolocation_api', __name__)
@geolocation_api.route('/geolocation', methods=['GET'])
def handle_geolocation():
    try:
        location_data = get_location_map()
        return jsonify({
            'success': True,
            'ip': location_data['ip'],
            'city': location_data['city'],
            'region': location_data['region'],
            'country': location_data['country'],
            'latitude': location_data['latitude'],
            'longitude': location_data['longitude'],
            'address': location_data['address'],
            'map_url': location_data['map_url']  # Provide the correct map URL
        })
    
    except Exception as e:
        print(f"Error: {str(e)}")  # Log the error to the console for easier debugging
        return jsonify({'success': False, 'message': str(e)}), 500
