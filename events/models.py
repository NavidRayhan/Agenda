from django.db import models
# Create your models here.

class Interview(models.Model):
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default=None)
    online = models.BooleanField(default=False)
    time = models.DateTimeField()

    def __str__(self):
        return "{0} at {1}".format(self.company, self.time)

