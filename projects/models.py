from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator

STATUS = (
    (1,"Live"),
    (0,"Completed"))

class Project(models.Model):
    number = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    company = models.CharField(max_length=200, null=True)
    contractor = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=8, null=True)
    value = models.DecimalField(max_digits=7, decimal_places=0)
    designer = models.ManyToManyField(User, related_name='pd')
    pm = models.ManyToManyField(User, related_name='pm')    
    website = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='uploads/img', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])], blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    
    class Meta:  
        db_table = "project"
        ordering = ['-number']
    #budget
    hourly_rate = models.IntegerField(default=35, validators=[MinValueValidator(0)])
    design_value_prelims = models.IntegerField(default=0, validators=[MaxValueValidator(99999999), MinValueValidator(0)])

    def designer_list(self):
        return ",".join([str(p) for p in self.designer.all()])
    def pm_list(self):
        return ",".join([str(p) for p in self.designer.all()])

    @property
    def get_created(self):
        return self.created.strftime("%m/%d/%Y, %H:%M:%S")
    
    def __str__(self):
        return "{} - {}".format(self.number, self.name)


class Phase(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True)
    is_fire = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    #design dates
    design_start = models.DateField(editable= True, default=datetime.today, blank=True)
    design_end = models.DateField(editable= True, default=datetime.today, blank=True)


    def get_start_date(self):
        return self.design_start.strftime('%d / %B / %Y')
    def get_end_date(self):
        return self.design_end.strftime('%d %B %Y')
    def get_updated_on(self):
        return self.updated_on.strftime('%d %B %Y')
    
    
    def __str__(self):
        return "{} - {} - {}".format(self.project, self.name, self.description)


EVENT_TYPE = (
    (0,"GA Issue"),
    (1,"GA Status"),
    (2,"TS Issue"),
    (3,"TS Status"),
    )
class Eventset(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    date = models.DateField(editable= True, default=datetime.today, blank=True)
    type = models.IntegerField(choices=EVENT_TYPE, default=0)
    message = models.TextField(max_length=500, blank = True, null=True)
    class Meta:          
        ordering = ['-date']