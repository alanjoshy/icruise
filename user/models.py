from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userdetails(models.Model):
    basic_data = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.TextField(max_length=100)
    Phone_Number = models.IntegerField()

