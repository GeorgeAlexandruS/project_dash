from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

POSITION = ((0,"Designer"),
    (1,"Senior Designer"),
    (2,"Project Design Manager"),
    (3,"Project Manager"),
    (4,"Senior Manager"))

class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField(choices=POSITION, default=0)
    avatar = models.ImageField(upload_to='uploads/img', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])], blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_created(self):
        return self.created.strftime("%m/%d/%Y, %H:%M:%S")
    
    def __str__(self):
        return "{} - {}".format(self.name, self.get_created)

    class Meta:  
        ordering = ['-name']