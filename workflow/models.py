from django.db import models
from projects.models import Phase
from profiles.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

DOC_TYPE = (
    (3,"Technical Submittal"),
    (4,"GAs and Detail"),
    (5,"Fabrication Drawing"),
    (7,"As Built"),)

class Document(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, default=None, related_name="document_list")
    number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200, null=True)
    type = models.IntegerField(choices=DOC_TYPE, default=4)
    designer = models.ForeignKey(User, on_delete=models.PROTECT)    
    withdrawn = models.BooleanField(default=False)
    class Meta:
        ordering = ['number']

    def __str__(self):
        return "{} - {} - {} - {}".format(self.phase.project.number, self.phase.name, self.number, self.type )


class Submission(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, default=None, related_name="submissions")
    date = models.DateField(editable=True, default=datetime.today, blank=False)    
    active = models.BooleanField(default=True)
    revision = models.CharField(max_length=3, default = 'P00')
    @property
    def get_date(self):
        return self.date.strftime("%d/%m/%Y")

    class Meta:
        ordering = ['date']
    
    def __str__(self):
       return "{} - {} - {}".format(self.document.phase.project.number, self.document.number, self.get_date)


STATUS = (
    (0,"A"),
    (1,"B"),
    (2,"C")
    )

class Status(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, default=None, related_name="comments")
    date = models.DateField(editable=True, default=datetime.today, blank=False)    
    status = models.IntegerField(choices=STATUS, default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['date']

    @property
    def get_date(self):
        return self.date.strftime("%d/%m/%Y")
    
    def __str__(self):
       return "{} - {} - {} - {} - {} - {}".format(self.submission.document.phase.project.number, self.submission.document.phase.name, self.submission.document.number, self.get_date, self.get_status_display(), self.active)
