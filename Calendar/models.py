from django.db import models
from events.models import *
from Tasks.models import *

class User(models.Model):
    username = models.CharField(max_length= 25)
    password = models.CharField(max_length= 25)
    gmail = models.EmailField(blank=True,null=True)


