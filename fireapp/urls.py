from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('about-us', views.about_us, name='about-us'),
    path('faq/', views.faq, name="faq"),
    path('contact/', views.contact, name="contact"),
   
]