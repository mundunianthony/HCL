# core/serializers.py
from django.contrib.auth import get_user_model  # Import get_user_model
from rest_framework import serializers

User = get_user_model()  # Use the custom user model

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Use the custom user model
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
