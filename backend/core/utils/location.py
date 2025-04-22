# core/utils/location.py
import requests

def get_user_location():
    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    loc = data.get('loc')  # "latitude,longitude"
    if loc:
        lat, lon = loc.split(',')
        return float(lat), float(lon)
    return None, None

def get_nearby_hospitals(lat, lon, radius=5000):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:{radius},{lat},{lon});
      way["amenity"="hospital"](around:{radius},{lat},{lon});
      relation["amenity"="hospital"](around:{radius},{lat},{lon});
    );
    out center;
    """
    response = requests.post(overpass_url, data={"data": query})
    data = response.json()
    hospitals = []
    for element in data['elements']:
        name = element.get('tags', {}).get('name', 'Unnamed Hospital')
        lat = element.get('lat') or element.get('center', {}).get('lat')
        lon = element.get('lon') or element.get('center', {}).get('lon')
        hospitals.append({
            'name': name,
            'latitude': lat,
            'longitude': lon,
        })
    return hospitals
