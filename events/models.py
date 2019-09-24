from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70,default=None)
    phone_num = models.IntegerField(default=None)

class Interview(models.Model):
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default=None)
    online = models.BooleanField(default=False)
    time = models.DateTimeField()
    people = models.ManyToManyField(Person)

    def __str__(self):
        return "{0} at {1}".format(self.company, self.time)

class Social(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    details = models.TextField()
    time = models.DateTimeField()

