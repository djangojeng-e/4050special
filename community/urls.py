from django.contrib import admin
from django.urls import path, include
from .views import community_page

urlpatterns = [
    path('', community_page, name='community_page'),
]
