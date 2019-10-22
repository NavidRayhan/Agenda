from django.db import models
from django.contrib.auth.models import User

class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default=None)
    online = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    people = models.TextField()
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return "{0} at {1}".format(self.company, self.start_time)


class Networking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    roles = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
