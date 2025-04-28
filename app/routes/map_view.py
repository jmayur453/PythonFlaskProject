from flask import Blueprint, render_template
import requests

map_view = Blueprint('map_view', __name__)

@map_view.route('/map')
def show_map():
    token = "e9349ffdb5b878"
    url = f"https://ipinfo.io/json?token={token}"

    res = requests.get(url)
    if res.status_code != 200:
        return f"Error fetching location: {res.status_code}", 500

    data = res.json()
    loc = data.get("loc", "0,0").split(",")
    lat, lon = float(loc[0]), float(loc[1])
    city = data.get("city", "Unknown")
    country = data.get("country", "Unknown")

    return render_template("map.html", lat=lat, lon=lon, city=city, country=country)
