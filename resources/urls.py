from django.contrib import admin
from django.urls import path, include
from .views import resource_list


urlpatterns = [
    path('', resource_list, name='resource_list'),
]
