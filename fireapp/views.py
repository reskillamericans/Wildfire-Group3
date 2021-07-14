from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import mail_admins, send_mail
from .forms import CreateNewEmailSubscription, SubmitQuestion
from .models import NewsletterEmailSub, Faq
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.method == 'POST':
        newsletter_sub_request(request)

    return render(request, "index.html")

def faq(request):
    context = {
        "questions" : Faq.objects.all()
    }

    if request.method == 'POST':
        newsletter_sub_request(request)

    return render(request, "faq.html", context)

def contact(request):
    if request.method == 'POST':
        if request.POST.__contains__("first_name"):
            form = SubmitQuestion(request.POST)
            if form.is_valid():

                receivers = []
                for user in User.objects.filter(is_superuser=True):
                    receivers.append(user.email)

                send_mail(
                    'New Question Received',
                    'A new question has been submitted. Please answer it as soon as possible',
                    None,
                    receivers,
                    fail_silently=False
                )

                form.save()
                messages.success(request, 'Your question has been submitted!')
                return redirect('index')
        else:
            newsletter_sub_request(request)
    
    context = {'contact': SubmitQuestion(), 'newsletter': CreateNewEmailSubscription()}

    return render(request, "contact.html", context)

def about_us(request):
    if request.method == 'POST':
        newsletter_sub_request(request)

    return render(request, "about-us.html")

def newsletter_sub_request(request):
 
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

def error_404(request, exception):
    return render(request, "404.html")
