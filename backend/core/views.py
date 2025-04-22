from django.shortcuts import render

# Create your views here.
# core/views.py
from django.http import JsonResponse
from .utils.location import get_user_location, get_nearby_hospitals

def nearby_hospitals(request):
    lat, lon = get_user_location()
    if lat and lon:
        hospitals = get_nearby_hospitals(lat, lon)
        return JsonResponse({'location': {'lat': lat, 'lon': lon}, 'hospitals': hospitals})
    else:
        return JsonResponse({'error': 'Unable to determine location'}, status=400)
