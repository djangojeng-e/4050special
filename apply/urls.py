from django.contrib import admin
from django.urls import path, include
from .views import index, application, terms_and_conditions



urlpatterns = [
    path('', index, name='index'),
    path('application', application, name='application'),
    path('application/terms_and_conditions', terms_and_conditions, name='terms_and_conditions')
]
