from django.shortcuts import render
from .models import Community_Post
# Create your views here.


def community_page(request):
    community_post = Community_Post.objects.all() 

    return render(request, 'community/community_page.html', {'community_post': community_post})