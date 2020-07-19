from django.shortcuts import render
from .models import Resource, Resourceimages

# Create your views here.


def resource_list(request):
    resources = Resource.objects.all() 
    
    content = {
        'resources': resources,
    }
    return render(request, 'resource/resource_list.html', content)