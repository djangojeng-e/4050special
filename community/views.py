from django.shortcuts import render, HttpResponse
from .models import Community_Post
from .forms import CommunicationForm
from django.contrib.auth.models import User
# Create your views here.


def community_page(request):
    if request.method == "POST":
        community_post = Community_Post.objects.all()
        form = CommunicationForm(request.POST)
        if form.is_valid():
            writer = User.objects.get(username=request.user.username)
            author = writer
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            print(writer)
            print(author)

            post = Community_Post(
                writer=writer,
                author=writer,
                title=title,
                content=content
            )
            post.save()
            print(content)
            community_post = Community_Post.objects.all()
        else:
            return HttpResponse('에러') 
    else:
        form = CommunicationForm()
        community_post = Community_Post.objects.all()
        return render(request, 'community/community_page.html', {'community_post': community_post, 'form': form})
    return render(request, 'community/community_page.html', {'community_post': community_post, 'form': form})