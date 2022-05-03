
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_bio = models.CharField(max_length=255)
    user_reputation = models.DecimalField(max_digits=3, decimal_places=1)
    is_verified = models.BooleanField()
    is_admin = models.BooleanField()
    user_photo = models.ImageField()
    user_theme = models.CharField(max_length=50)
    join_date = models.DateField()
