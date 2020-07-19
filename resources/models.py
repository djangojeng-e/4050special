from django.db import models
from apply.models import Members

# Create your models here.


class Resource(models.Model):
    author = models.ForeignKey(Members, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='자료 타이틀', blank=True)
    content = models.TextField(verbose_name='자료내용', blank=True)
    date_created = models.DateField(auto_now_add=True, verbose_name='작성날짜')
    view_counts = models.IntegerField(verbose_name='조회수', default=0)

    class Meta:
        verbose_name = "자료실"
        verbose_name_plural = "자료실"

class Resourceimages(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='resources/images/%Y/%m', blank=True)


class Resourcefiles(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    files = models.FileField(upload_to='resources/files/%Y/%m', blank=True)


class ResourceViews(models.Model):
    viewer = models.ForeignKey(Members, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)






