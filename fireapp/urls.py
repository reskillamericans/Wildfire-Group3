from django.urls import path
from . import views
from .views import renderform,submitForm
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about-us')
]