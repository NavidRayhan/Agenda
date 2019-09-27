from django import forms
from .models import Interview, Social, Networking

class InterviewForm(forms.ModelForm):
    
    class Meta:
        model = Interview
        fields = ('company','location', 'online', 'start_time', 'end_time', 'people', 'notes')