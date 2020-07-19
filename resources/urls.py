from django.contrib import admin
from django.urls import path, include
from .views import resource_list, resource_detail


urlpatterns = [
    path('', resource_list, name='resource_list'),
    path('detail/<int:pk>', resource_detail, name="resource_detail"),
]
