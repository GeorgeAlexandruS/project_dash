# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type', 'name')
    search_fields = ['name']
 
admin.site.register(Company, CompanyAdmin)