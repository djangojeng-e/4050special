from django.contrib import admin
from django.urls import path, include
from .views import index, application, registration



urlpatterns = [
    path('', index, name='index'),
    path('application', application, name='application'),
    path('application/register', registration, name="registration"),
]
