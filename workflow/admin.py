from django.contrib import admin

from .models import Document, Submission, Status
# Register your models here.

admin.site.register(Document)
admin.site.register(Submission)
admin.site.register(Status)