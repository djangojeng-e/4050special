from django.contrib import admin
from .models import Members

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 
                    'address', 'country_residence', 'occupation',
                    'nationality', 'phone_number', 'email', 'member_level')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Members, MemberAdmin)