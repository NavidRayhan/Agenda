from django.db import models
from Classes.models import Course
import json
# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)
    worth = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField()
    
    def __str__(self):
        return "{0} on: {1}".format(self.course, self.start_time)

class CodingChallenge(models.Model):
    company = models.CharField(max_length=50)
    due_by = models.DateTimeField()
    completed_status = models.BooleanField(default=False)
    notes = models.TextField()

    def __str__(self):
        return "{0} due by: {1}".format(self.company, self.due_by)

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    course = models.OneToOneField(Course, on_delete= models.PROTECT, blank=True,null=True)
    due_by = models.DateTimeField()
    notes = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return "{0} due by: {1}".format(self.name, self.due_by)

class Other(models.Model):
    name = models.CharField(max_length=80)
    due_by = models.DateTimeField()
    notes = models.TextField()

    
    def __str__(self):
        return "{0} due by: {1}".format(self.name, self.due_by)

class DailyTask(models.Model):
    name = models.CharField(max_length=60)
    repeating = models.BooleanField(default=False)
    days = models.CharField(max_length=200, blank=True, null=True)
    

    def set_days(self, x):
        self.days = json.dumps(x)
    
    def get_days(self):
        return json.loads(self.days)    