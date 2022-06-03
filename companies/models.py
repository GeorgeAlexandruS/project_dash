from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator

TYPE = (
    (1,"Division"),
    (2,"Contractor"),
    (3,"Supplier"))

class Company(models.Model):
    name = models.CharField(max_length=200, null=True)
    type = models.IntegerField(choices=TYPE, default=1)
    website = models.URLField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:  
        db_table = "company"
        ordering = ['-id']

    def __str__(self):
        return "{} | {}".format(self.name, self.get_type_display())