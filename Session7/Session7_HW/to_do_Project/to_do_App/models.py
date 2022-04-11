from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class To_do(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateField(default=timezone.now)


    def __str__(self):
        return self.title

    def dday(self):
        remains = (self.deadline-timezone.now().date()).days
        if remains > 0:
            return "D-" + str(remains)
        elif remains == 0:
            return "D-Day"
        else:
            return "D+" + str(abs(remains))

    class Meta:
        ordering = ['deadline']
        