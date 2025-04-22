from django.shortcuts import render

# Create your views here.
# core/views.py
from django.http import JsonResponse
from .utils.location import get_user_location, get_nearby_hospitals
from rest_framework import generics
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model  # Import get_user_model
from rest_framework.permissions import AllowAny

def nearby_hospitals(request):
    lat, lon = get_user_location()
    if lat and lon:
        hospitals = get_nearby_hospitals(lat, lon)
        return JsonResponse({'location': {'lat': lat, 'lon': lon}, 'hospitals': hospitals})
    else:
        return JsonResponse({'error': 'Unable to determine location'}, status=400)

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()  # Use get_user_model to reference the custom user model
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
