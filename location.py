import requests

def get_location():
    data = requests.get("https://ipapi.co/json/").json()
    lat, lon = data['latitude'], data['longitude']
    maps = f"https://www.google.com/maps?q={lat},{lon}"
    return maps
