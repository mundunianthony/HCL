# core/urls.py
from django.urls import path
from .views import nearby_hospitals, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('nearby-hospitals/', nearby_hospitals, name='nearby-hospitals'),
]
