from django.contrib import admin

# Register your models here.
from .models import  Interview, Networking

admin.site.register(Interview)
admin.site.register(Networking)