from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CodingChallenge)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(DailyTask)
admin.site.register(Other)