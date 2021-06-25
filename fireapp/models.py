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
    registration_date = models.DateTimeField()

class EmergencyContact(models.Model):
    registered_user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mark_safe = models.BooleanField()
    need = models.CharField(max_length=300)
    date_added = models.DateTimeField()

class Question(models.Model):
    registered_user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    post_date = models.DateTimeField()
    

class FireIncident(models.Model):
    incident_description = models.CharField(max_length=300)
    incident_location = models.CharField(max_length=300)
    incident_date = models.DateTimeField()
    reporter_first_name = models.CharField(max_length=50)
    reporter_last_name = models.CharField(max_length=50)
    reporter_contact_info = models.CharField(max_length=15)
<<<<<<< HEAD
    # incident_image = models.ImageField()

class NewsletterEmailSub(models.Model):
    email = models.EmailField(unique=True)
    sign_up_date = models.DateTimeField()
=======
    # incident_image = models.ImageField()
>>>>>>> 4593361d555e31f124afc735fce128368d789a9e
