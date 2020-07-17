from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, reverse
from .models import Community_Post, Likes, Dislikes
from .forms import CommunicationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.


def community_page(request):
    if request.method == "POST":
        form = CommunicationForm(request.POST)
        if form.is_valid():
            writer = User.objects.get(username=request.user.username)
            author = writer
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            post = Community_Post(
                writer=writer,
                author=writer,
                title=title,
                content=content
            )
            post.save()
            
            community_post = Community_Post.objects.all().order_by('-id')
            paginator = Paginator(community_post, 10)

            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'community/community_page.html', {'community_post': community_post, 'form': form, 'page_obj': page_obj})
        else:
            return HttpResponse('에러') 
    else:
        form = CommunicationForm()
        community_post = Community_Post.objects.all().order_by('-id')
        paginator = Paginator(community_post, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'community/community_page.html', {'community_post': community_post, 'form': form, 'page_obj': page_obj})
    return render(request, 'community/community_page.html', {'community_post': community_post, 'form': form})


def post_like(request, pk):
    post = Community_Post.objects.get(id=pk)
    user = request.user
    if Likes.objects.filter(post=post, user=user): 
        return HttpResponseRedirect(reverse('community_page'))
    else: 
        like = Likes(post=post, user=user)
        like.save()
        post.like_counts += 1 
        post.save()
        return HttpResponseRedirect(reverse('community_page'))


def post_dislike(request, pk):
    post = Community_Post.objects.get(id=pk)
    user = request.user 
    if Dislikes.objects.filter(post=post, user=user):
        return HttpResponseRedirect(reverse('community_page'))
    else:
        dislike = Dislikes(post=post, user=user)
        dislike.save()
        post.dislike_counts =+ 1
        post.save()
        return HttpResponseRedirect(reverse('community_page'))

