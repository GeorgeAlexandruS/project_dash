# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Project, Phase, Eventset

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'contractor', 'value', 'status')
    list_filter = ('pm', 'status')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('number','name')}  
admin.site.register(Project, ProjectAdmin)

class PhaseAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'description')
    list_filter = ('project', 'is_fire', 'designer',)
    search_fields = ['project']
admin.site.register(Phase, PhaseAdmin)

class EventsetAdmin(admin.ModelAdmin):
    list_display = ('phase', 'type', 'date')
    list_filter = ('phase', 'type')
    search_fields = ['phase']
admin.site.register(Eventset, EventsetAdmin)

