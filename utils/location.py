import requests

def get_ip_and_location():
    try:
        res = requests.get("https://ipinfo.io/json", timeout=5)
        data = res.json()

        ip = data.get("ip", "Unknown")
        city = data.get("city", "")
        region = data.get("region", "")
        country = data.get("country", "")
        loc = data.get("loc")  # "lat,lon"

        if loc:
            lat, lon = loc.split(",")
            location_text = f"{city}, {region}, {country}"
            return ip, lat, lon, location_text

    except:
        pass

    return "Unknown", None, None, "Location unavailable"
