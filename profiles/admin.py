from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_filter = ('name', 'position')
    search_fields = ['name'] 
admin.site.register(Profile, ProfileAdmin)
