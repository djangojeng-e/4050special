from django.contrib import admin
from django.urls import path, include
from .views import community_page, post_like, post_dislike
from .views import SortbyAnnouncement, SortbyComments, SortbyDatecreated, SortbyLikes, SortbyViews
from .views import PostDetail

urlpatterns = [
    path('', community_page, name='community_page'),
    path('like/<int:pk>', post_like, name='post_like'),
    path('dislike/<int:pk>', post_dislike, name='post_dislike'),
    path('announcement', SortbyAnnouncement.as_view(), name='community_announcement'),
    path('date_created', SortbyDatecreated.as_view(), name='community_datecreated'),
    path('view_counts', SortbyViews.as_view(), name='community_viewcounts'),
    path('comment_counts', SortbyComments.as_view(), name='community_comments'),
    path('community_likes', SortbyLikes.as_view(), name='community_likes'),
    path('detail/<int:pk>', PostDetail, name='post_detail'),
]
