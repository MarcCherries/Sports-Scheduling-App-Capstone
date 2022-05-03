from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    location_coordinates = models.DecimalField(max_digits=20, decimal_places=4)
    location_info = models.CharField(max_length=255)