from fireapp.models import EmergencyContact
from django.contrib import admin
from .models import RegisteredUser, EmergencyContact, Question, FireIncident, NewsletterEmailSub, Faq, Contact
# Register your models here.
admin.site.register(RegisteredUser)
admin.site.register(EmergencyContact)
admin.site.register(Question)
admin.site.register(FireIncident)
admin.site.register(NewsletterEmailSub)
admin.site.register(Faq)
admin.site.register(Contact)