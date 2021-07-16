from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField
from datetime import datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from django.urls import reverse

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
    # incident_image = models.ImageField()
    
class NewsletterEmailSub(models.Model):
    email = models.EmailField(unique=True)
    sign_up_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"

class Faq(models.Model):
    title = models.CharField(max_length=150)
    response = models.TextField()

    def __str__(self):
        return f"{self.title}"
    def get_absolute_url(self):
        return reverse('fireapp:search', args=[self.id,])

class Contact(models.Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField(max_length=100)
    # error message when a wrong format entered
    phone_message = 'Phone number must be entered in the format: 999999999' 
    # your desired format 
    phone_regex = RegexValidator(
        regex=r'^\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$',
        message=phone_message
    )
    phone = models.CharField(validators=[phone_regex], max_length=60,
                             null=True, blank=True)
    state = CharField(max_length=50, blank=True, null=True)
    message = CharField(max_length=200)
    time_posted = DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.time_posted}"
