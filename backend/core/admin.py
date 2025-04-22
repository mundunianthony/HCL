from django.contrib import admin

# Register models
from django.contrib import admin
from .models import User, HealthCenter, Emergency

admin.site.register(User)
admin.site.register(HealthCenter)
admin.site.register(Emergency)
