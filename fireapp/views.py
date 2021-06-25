from django.shortcuts import render
from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import NewsletterEmailSub
from .forms import CreateNewEmailSubscription

# Create your views here.

def index(request):
    return HttpResponse("<h1>Wildfire App 3</h1>")

def newsletter(request):
    

    if request.method == 'POST':
        form = CreateNewEmailSubscription(request.POST)

        if form.is_valid():
            new_email = form.cleaned_data["email"]
            new_sub = CreateNewEmailSubscription(email=new_email)
            new_sub.save()
            
       
 
        
    return render(request, "fireapp/newsletter.html", {"form": form})
    