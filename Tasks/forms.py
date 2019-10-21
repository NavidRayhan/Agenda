from django import forms
from .models import CodingChallenge, Assignment

class AddCodingChallengeForm(forms.ModelForm):

    class Meta:
        model = CodingChallenge
        fields = ('company','due_by','notes')

class AddAssignmentForm(forms.ModelForm):

    class Meta:
        model=  Assignment
        fields = ('name', 'due_by', 'notes')
