from django import forms
from .models import *


class GoogleCalendarForm(forms.ModelForm):

    class Meta:
        model = GoogleCalendar
        fields = ('yes_no',)