from django.shortcuts import render

# Create your views here.


def resource_list(request):
    return render(request, 'resource/resource_list.html')