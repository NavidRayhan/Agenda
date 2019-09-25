from django.contrib import admin

# Register your models here.
from .models import Person, Interview, Networking, Social

admin.site.register(Person)
admin.site.register(Interview)
admin.site.register(Networking)
admin.site.register(Social)