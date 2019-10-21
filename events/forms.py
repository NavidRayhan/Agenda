from django import forms
from .models import Interview, Networking

class InterviewForm(forms.ModelForm):
    
    class Meta:
        model = Interview
        fields = ('company','location', 'online', 'start_time', 'end_time', 'people', 'notes')

class DeleteForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ('company', 'start_time')

class NetworkingForm(forms.ModelForm):
    class Meta:
        model = Networking
        fields = ('company','location', 'roles', 'description', 'start_time', 'end_time')