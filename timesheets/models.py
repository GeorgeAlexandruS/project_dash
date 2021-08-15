from django.db import models
from projects.models import Phase
from profiles.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

DESIGN_ACTIVITY = ((0,"Survey"),
    (1,"Intenal Design Meeting"),
    (2,"External Design Meeting"),
    (3,"Technical Submittals"),
    (4,"GA Drawings"),
    (5,"Fab Drawings"),
    (6,"Revisions"),
    (7,"As Builts"),)

class Timesheet(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, default=None)
    date = models.DateField(editable=True, default=datetime.today, blank=True)
    time_spent = models.IntegerField(default=None, validators=[MaxValueValidator(8), MinValueValidator(1)])
    activity = models.IntegerField(choices=DESIGN_ACTIVITY, default=4)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-date']

    @property
    def get_date(self):
        return self.date.strftime("%d/%m/%Y")

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.phase.project.number, self.phase.name, self.user.first_name, self.get_date, self.time_spent )
