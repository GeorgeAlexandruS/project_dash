# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Project, Phase, Eventset

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'contractor', 'status')
    list_filter = ('designer', 'pm', 'status')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('number','name')}  
admin.site.register(Project, ProjectAdmin)

class PhaseAdmin(admin.ModelAdmin):
    list_display = ('project', 'name')
    list_filter = ('project', 'is_fire')
    search_fields = ['project']
admin.site.register(Phase, PhaseAdmin)

class EventsetAdmin(admin.ModelAdmin):
    list_display = ('phase', 'type', 'date')
    list_filter = ('phase', 'type')
    search_fields = ['phase']
admin.site.register(Eventset, EventsetAdmin)

