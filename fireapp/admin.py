from fireapp.models import EmergencyContact
from django.contrib import admin
from .models import RegisteredUser, EmergencyContact, Question, FireIncident, NewsletterEmailSub
# Register your models here.
admin.site.register(RegisteredUser)
admin.site.register(EmergencyContact)
admin.site.register(Question)
admin.site.register(FireIncident)
admin.site.register(NewsletterEmailSub)
