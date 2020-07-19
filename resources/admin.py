from django.contrib import admin
from .models import Resource, Resourcefiles, Resourceimages, ResourceViews

# Register your models here.


class ResourceimagesInline(admin.TabularInline):
    model = Resourceimages


class ResourcefilesInline(admin.TabularInline):
    model = Resourcefiles


class ResourceAdmin(admin.ModelAdmin):
    inlines = [ResourceimagesInline, ResourcefilesInline]
    list_display = ('author', 'title', 'content', 'date_created', 'view_counts')
    list_filter = ['title']
    search_fields = ['author']


admin.site.register(Resource, ResourceAdmin)