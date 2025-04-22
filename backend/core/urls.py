# core/urls.py
from django.urls import path
from .views import nearby_hospitals

urlpatterns = [
    path('nearby-hospitals/', nearby_hospitals, name='nearby-hospitals'),
]
