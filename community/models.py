from django.db import models
from datetime import date
import datetime
from datetime import timedelta
from apply.models import Members
from django.contrib.auth.models import User

# Create your models here.


class Community_Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    author = models.CharField(blank=True, max_length=100)
    title = models.CharField(max_length=100, verbose_name='글 제목', blank=True)
    content = models.TextField(blank=True, verbose_name='글내용')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='등록타임')
    post_views = models.IntegerField(default=0, verbose_name='조회수')
    like_counts = models.IntegerField(default=0, verbose_name='좋아요 갯수')
    dislike_counts = models.IntegerField(default=0, verbose_name='싫어요 갯수')
    is_announcement = models.BooleanField(null=True, verbose_name='공지사항?')

    # def get_author(self):
    #     author_name = User.objects.get(username=request.user.username)
    #     return author_name

    def lapsed_time(self):
        pass
        

    def comments_counts(self):
        comments = self.comments_set.all()
        comments_count = comments.count() 
        return comments_count


    class Meta:
        verbose_name = '소통실 글'
        verbose_name_plural ='소통실 글'


class Comments(models.Model):
    post = models.ForeignKey(Community_Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        verbose_name = '소통실 댓글'
        verbose_name = '소통실 댓글'



    