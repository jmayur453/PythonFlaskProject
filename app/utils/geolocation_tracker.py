import ipinfo
import folium
from geopy.geocoders import Nominatim
import os

def get_location_map():
    access_token = 'e9349ffdb5b878'  # Replace with your actual token
    handler = ipinfo.getHandler(access_token)

    try:
        details = handler.getDetails()
    except ipinfo.exceptions.RequestError as e:
        print(f"RequestError: {str(e)}")
        return {
            "success": False,
            "message": "Failed to fetch location data. Please check the API token and rate limits."
        }
    except Exception as e:
        print(f"Error while getting location data: {str(e)}")
        return {
            "success": False,
            "message": "Failed to fetch location data due to an unknown error."
        }

    ip = details.ip
    city = details.city
    region = details.region
    country = details.country_name
    loc = details.loc  # "latitude,longitude"
    latitude, longitude = map(float, loc.split(','))

    # Reverse geocoding for additional details
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{latitude}, {longitude}")

    # Create map
    map_obj = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup=f"Your Location: {city}, {country}").add_to(map_obj)

    # Create a directory to save the map if it doesn't exist
    map_dir = os.path.join(os.getcwd(), 'static/maps')
    os.makedirs(map_dir, exist_ok=True)

    map_filename = f"{ip}_location_map.html"
    map_path = os.path.join(map_dir, map_filename)
    map_obj.save(map_path)
    print(f"Map saved at: {map_path}")  # Debugging map saving location

    return {
        "success": True,
        "ip": ip,
        "city": city,
        "region": region,
        "country": country,
        "latitude": latitude,
        "longitude": longitude,
        "address": location.address if location else "Unknown",
        "map_url": f"/static/maps/{map_filename}"  # Correct URL for the saved map
    }