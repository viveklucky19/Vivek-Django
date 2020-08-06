from django.db import models
import datetime
from django.utils import timezone


class AllCourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length=100)
    startedFrom = models.DateTimeField("Started From")

    def __str__(self):
        return self.coursename
    
    def was_published_recently(self):
        return self.startedFrom >= timezone.now() - datetime.timedelta(days=1)

class details(models.Model):
    course = models.ForeignKey(AllCourses,on_delete=models.CASCADE)
    ct = models.CharField(max_length=500)
    your_choice = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ct)

