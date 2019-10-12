from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

class taskView(TemplateView):

    model = CodingChallenge
    template_name = "Tasks/tasks.html"
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["coding_challenges"] = CodingChallenge.objects.all()
        context["assignments"] = Assignment.objects.all()
        context['daily_tasks'] = DailyTask.objects.all()
        context['exams'] = Exam.objects.all()
        context['other'] = Other.objects.all()
        return context
        