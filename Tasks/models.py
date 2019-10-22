from django.db import models
from Classes.models import Course
import json
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=65)
    notes = models.TextField(null=True, blank=True)
    task_type = models.CharField(max_length=65)
    due_by = models.DateTimeField()
    
    def __str__(self):
        return "{0} due by: {1}".format(self.name, self.due_by)