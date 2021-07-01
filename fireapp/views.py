from django.contrib import messages
from django.shortcuts import render
from django.core.mail import mail_admins, send_mail
from .forms import CreateNewEmailSubscription
from .models import NewsletterEmailSub, Faq

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CreateNewEmailSubscription(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data["email"]
            

            # Check if email is already in database
            email_sub =  NewsletterEmailSub.objects.get_or_create(email=new_email)
            if email_sub[1]:
                messages.info(request, "Thank you for subscribing.")
                email_sub[0].save()

                message = "Here is your newsletter subcription confirmation."
                send_mail("Newsletter Subscription", message, None, recipient_list = [new_email])

                message = f'{new_email} has been added to the newsletter mailing list'
                mail_admins("New Newsletter Subscriber", message)
            else:
                messages.info(request, "You are already subscribed")

    return render(request, "index.html")

def faq(request):
    context = {
        "questions" : Faq.objects.all()
    }

    return render(request, "faq.html", context)



    
    
