from django.contrib import admin
from django.urls import path, include
from .views import community_page, post_like, post_dislike

urlpatterns = [
    path('', community_page, name='community_page'),
    path('like/<int:pk>', post_like, name='post_like'),
    path('dislike/<int:pk>', post_dislike, name='post_dislike'),
]
