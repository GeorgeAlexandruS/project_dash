# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Timesheet

class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('user', 'phase', 'activity', 'time_spent')
    list_filter = ('user', 'activity')
    search_fields = ['activity']

admin.site.register(Timesheet, TimesheetAdmin)
