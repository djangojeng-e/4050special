from django.shortcuts import render

# Create your views here.


def community_page(request):
    return render(request, 'community/community_page.html')