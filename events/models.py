from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, max_length=70,blank=True)
    phone_num = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        if self.email !=None:
            return "{0} ({1})".format(self.name,self.email)
        elif self.company:
            return "{0} ({1})".format(self.name, self.company)
        else:
            return self.name
class Interview(models.Model):
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default=None)
    online = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    people = models.ManyToManyField(Person)

    def __str__(self):
        return "{0} at {1}".format(self.company, self.start_time)

class Social(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    details = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True, blank=True)
    end_time = models.DateTimeField(auto_now_add=True, blank=True)

class Networking(models.Model):
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    roles = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=True, blank=True)
    end_time = models.DateTimeField(auto_now_add=True, blank=True)
    
