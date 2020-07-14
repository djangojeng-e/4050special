from django.contrib import admin
from .models import Community_Post, Comments
# Register your models here.


class Community_PostAdmin(admin.ModelAdmin):
    list_display = ('writer', 'content', 'date_created', 'post_views', 'like_counts', 'dislike_counts', 'is_announcement') 



admin.site.register(Community_Post, Community_PostAdmin)
admin.site.register(Comments)
# admin.site.register(Community_likes)
# admin.site.register(Community_dislikes)

