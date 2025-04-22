from django.db import models

# core/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# --------------------------------------------
# 1. Custom User Model
# --------------------------------------------
class User(AbstractUser):
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    emergency_contacts = models.JSONField(default=list, blank=True)
    medical_conditions = models.JSONField(default=list, blank=True)
    allergies = models.JSONField(default=list, blank=True)
    medications = models.JSONField(default=list, blank=True)
    preferred_health_center = models.ForeignKey(
        'HealthCenter',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

# --------------------------------------------
# 2. Health Center Model
# --------------------------------------------
class HealthCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)  # Address or coordinates
    services_offered = models.JSONField(default=list, blank=True)
    contact_info = models.CharField(max_length=100)
    available_ambulances = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# --------------------------------------------
# 3. Emergency Model
# --------------------------------------------
class Emergency(models.Model):
    SEVERITY_CHOICES = [
        ('emergency', 'Emergency'),
        ('urgent', 'Urgent'),
        ('routine', 'Routine'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    time_reported = models.DateTimeField(auto_now_add=True)
    condition_type = models.CharField(max_length=255, blank=True, null=True)
    severity_level = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    allergies = models.JSONField(default=list, blank=True)
    preexisting_conditions = models.JSONField(default=list, blank=True)
    medications = models.JSONField(default=list, blank=True)
    preferred_health_center = models.ForeignKey(
        HealthCenter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    transportation_needs = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Emergency - {self.user.username} ({self.severity_level})"
