from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddCodingChallengeForm, AddAssignmentForm
from datetime import timedelta, datetime
from django.utils import timezone
# Create your views here.

class tasks:
    def __init__(self, model, color):
        self.model = model
        self.color = color

class taskView(TemplateView):

    
    model = CodingChallenge
    template_name = "Tasks/tasks.html"
    AddAssignmentForm = AddAssignmentForm
    AddCodingChallengeForm = AddCodingChallengeForm

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super().get_context_data(**kwargs)
        context["tasks"] = []

        for i in CodingChallenge.objects.all():
            if now > i.due_by + timedelta(days=30):
                i.delete() 
            context["tasks"].append(tasks(model=i,color="rgb(80, 5, 5)"))
        for i in Assignment.objects.all():
            #if now > i.due_by + timedelta(days=30):
            #    i.delete() 
            context["tasks"].append(tasks(model=i,color="rgb(5, 129, 129)"))
        for i in Exam.objects.all():
            if now > i.start_time  + timedelta(days=30):
                i.delete() 
            context["tasks"].append(tasks(model=i,color="green"))
        for i in Other.objects.all():
            if now > i.due_by + timedelta(days=30):
                i.delete() 
            context["tasks"].append(tasks(model=i,color="red"))
        
        temp = []
        for j in range(len(context["tasks"])-1):
            for i in range(len(context["tasks"])-1):
                if context["tasks"][i].model.due_by > context["tasks"][i+1].model.due_by:
                    tempval = context["tasks"][i]
                    context["tasks"][i] = context["tasks"][i+1]
                    context["tasks"][i+1] = tempval

        return context
        
    def post(self, request, *args, **kwargs):
        
        form = self.AddCodingChallengeForm(request.POST)

        #make record
        if form.is_valid():
            company = form['company'].value()
            due_by = form['due_by'].value()
            notes = form['notes'].value()

            try:
                CodingChallenge.objects.all().filter(company=company, 
                due_by__gte= due_by, due_by__lte=due_by+":59+00:00")[0].delete()
                return HttpResponseRedirect(request.path)
            except:
                a = CodingChallenge(company=company, due_by=due_by, notes=notes)
                a.save()
                return HttpResponseRedirect(request.path)
        
        form = self.AddAssignmentForm(request.POST)
        
        #make record
        if form.is_valid():
            name = form['name'].value()
            due_by = form['due_by'].value()
            notes = form['notes'].value()

            try:
                Assignment.objects.all().filter(name=name, 
                due_by__gte= due_by, due_by__lte=due_by+":59+00:00")[0].delete()
                return HttpResponseRedirect(request.path)
            except:
                a = Assignment(name=name, due_by=due_by, notes=notes)
                a.save()
                return HttpResponseRedirect(request.path)
        return HttpResponseRedirect(request.path)