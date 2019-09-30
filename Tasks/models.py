from django.db import models
from Classes.models import Course
# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)
    worth = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField()

class CodingChallenge(models.Model):
    company = models.CharField(max_length=50)
    due_by = models.DateTimeField()
    completed_status = models.BooleanField(default=False)
    allowed_time = models.DateTimeField()
    notes = models.TextField()

class Assignment(models.Model):
    course = models.OneToOneField(Course, on_delete= models.PROTECT, blank=True,null=True)
    due_by = models.DateTimeField()

class Other(models.Model):
    due_by = models.DateTimeField()
    notes = models.TextField()