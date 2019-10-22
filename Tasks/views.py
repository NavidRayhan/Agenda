from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddCodingChallengeForm, AddAssignmentForm
from datetime import timedelta, datetime
from django.utils import timezone
from .utils import tasks, mergeSort
from django.contrib.auth.models import User


class taskView(TemplateView):

    model = CodingChallenge
    template_name = "Tasks/tasks.html"
    AddAssignmentForm = AddAssignmentForm
    AddCodingChallengeForm = AddCodingChallengeForm

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super().get_context_data(**kwargs)
        context["tasks"] = []
        if self.request.user.id == None:
            for i in CodingChallenge.objects.filter(user__id=1):
                context["tasks"].append(tasks(model=i,color="rgb(80, 5, 5)"))
            
            for i in Assignment.objects.filter(user__id=1):
                context["tasks"].append(tasks(model=i,color="rgb(5, 129, 129)"))
                
            for i in Exam.objects.filter(user__id=1):
                context["tasks"].append(tasks(model=i,color="green"))
            
            for i in Other.objects.filter(user__id=1):
                context["tasks"].append(tasks(model=i,color="red"))
        else:
        #tasks will expire and auto delete after 30 days, all task models added to a master class 
            for i in CodingChallenge.objects.filter(user__id=self.request.user.id):
                if now > i.due_by + timedelta(days=30): i.delete() 
                context["tasks"].append(tasks(model=i,color="rgb(80, 5, 5)"))
            
            for i in Assignment.objects.filter(user__id=self.request.user.id):
                if now > i.due_by + timedelta(days=30): i.delete() 
                context["tasks"].append(tasks(model=i,color="rgb(5, 129, 129)"))
                
            for i in Exam.objects.filter(user__id=self.request.user.id):
                if now > i.start_time  + timedelta(days=30): i.delete() 
                context["tasks"].append(tasks(model=i,color="green"))
            
            for i in Other.objects.filter(user__id=self.request.user.id):
                if now > i.due_by + timedelta(days=30): i.delete() 
                context["tasks"].append(tasks(model=i,color="red"))
            
        #sorting events by earliest 
        mergeSort(context["tasks"])        
        
        return context
        
    def post(self, request, *args, **kwargs):
        
        if self.request.user.id == None:
            return HttpResponse("<script> window.confirm('You must log in to edit Tasks!'); window.location.href = '../tasks' </script>") 
        form = self.AddCodingChallengeForm(request.POST)

        #make record
        if form.is_valid():
            company = form['company'].value()
            due_by = form['due_by'].value()
            notes = form['notes'].value()

            try:
                CodingChallenge.objects.all().filter(company=company, due_by__gte= due_by, 
                due_by__lte=due_by+":59+00:00", user__id=request.user.id)[0].delete()
                return HttpResponseRedirect(request.path)
            except:
                a = CodingChallenge(company=company, due_by=due_by, notes=notes, user=request.user)
                a.save()
                return HttpResponseRedirect(request.path)
        
        form = self.AddAssignmentForm(request.POST)
        
        #make record
        if form.is_valid():
            name = form['name'].value()
            due_by = form['due_by'].value()
            notes = form['notes'].value()

            try:
                Assignment.objects.all().filter(name=name, due_by__gte= due_by, 
                due_by__lte=due_by+":59+00:00", user__id=request.user.id)[0].delete()
                return HttpResponseRedirect(request.path)
            except:
                a = Assignment(name=name, due_by=due_by, notes=notes, user=request.user)
                a.save()
                return HttpResponseRedirect(request.path)
        return HttpResponseRedirect(request.path)