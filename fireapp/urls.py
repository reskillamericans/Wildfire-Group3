from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('about/', views.about_us, name='about'),
    path('faq/', views.faq, name="faq"),
    path('contact/', views.contact, name="contact"),
]