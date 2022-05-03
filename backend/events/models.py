from django.db import models
from users.models import User
from locations.models import Location

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    event_type = models.CharField(max_length=50)
    event_description = models.CharField(max_length=255)
    event_specialInstructions = models.CharField(max_length=255)
    experience_level = models.CharField(max_length=50)