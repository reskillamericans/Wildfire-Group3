from django.db import models
from django.db.models.fields import IntegerField
from datetime import datetime

# Create your models here.

class RegisteredUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    registration_date = models.DateField(default = datetime.today)

class EmergencyContact(models.Model):
    registered_user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mark_safe = models.BooleanField()
    need = models.CharField(max_length=300)
    date_added = models.DateField(default = datetime.today)

class Question(models.Model):
    registered_user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    post_date = models.DateField(default = datetime.today)
    

class GuestUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guest_email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    

class FireIncident(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(null=True)
    location = models.CharField(max_length=300)
    incident_date = models.DateField(default = datetime.today)
