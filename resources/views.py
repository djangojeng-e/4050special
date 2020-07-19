from django.shortcuts import render
from .models import Resource, Resourceimages
from apply.models import Members

# Create your views here.


def resource_list(request):
    resources = Resource.objects.all() 
    
    content = {
        'resources': resources,
    }
    return render(request, 'resource/resource_list.html', content)


def resource_detail(request, pk): 
    user = request.user.username 
    resource = Resource.objects.filter(id=pk)
    if resource:
        resource.view_counts += 1
        resource.save()
        return render(request, 'resource/resource_detail.html', {'resource': resource})
    else:
        return render(request, 'resource/resource_detail.html')
    