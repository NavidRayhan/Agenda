from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_type','name','due_by','notes')

