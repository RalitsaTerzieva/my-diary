# TODO: create a UserProfile model to store additional user fields with foreign key to django.contrib.auth.models.User

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_day = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone = models.IntegerField()
