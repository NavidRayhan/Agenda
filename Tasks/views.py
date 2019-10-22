from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddTaskForm
from datetime import timedelta, datetime
from django.utils import timezone
from .utils import TaskObject, mergeSort
from django.contrib.auth.models import User


class taskView(TemplateView):

    model = Task
    template_name = "tasks/tasks.html"
    AddTaskForm = AddTaskForm

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super().get_context_data(**kwargs)
        context["tasks"] = []
        if self.request.user.id == None:
            for i in Task.objects.filter(user__id=1):
                context["tasks"].append(TaskObject(model=i,task_type=i.task_type))
        else:
        #tasks will expire and auto delete after 30 days, all task models added to a master class 
            for i in Task.objects.filter(user__id=self.request.user.id):
                if now > i.due_by + timedelta(days=30): i.delete() 
                context["tasks"].append(TaskObject(model=i,task_type=i.task_type))
        #sorting events by earliest 
        mergeSort(context["tasks"])        
        
        return context
        
    def post(self, request, *args, **kwargs):
        
        if self.request.user.id == None:
            return HttpResponse("<script> window.confirm('You must log in to edit Tasks!');"+
            "window.location.href = '../tasks' </script>") 
        
        #delete record
        try:
            form = self.AddTaskForm(request.POST)
            name = form['name'].value().strip()
            due_by = form['due_by'].value().strip() 
            if len(Task.objects.all().filter(name=name, due_by__gte= due_by, 
            due_by__lte=due_by+":59+00:00", user__id=request.user.id)) == 0:
                None.strip()
            Task.objects.all().filter(name=name, due_by__gte= due_by, 
            due_by__lte=due_by+":59+00:00", user__id=request.user.id).delete()
            return HttpResponseRedirect(request.path)
        except:
            pass
        
        #make record
        if form.is_valid():
            name = form['name'].value().strip()
            due_by = form['due_by'].value().strip()
            notes = form['notes'].value()
            task_type = form['task_type'].value()
            a = Task(task_type= task_type, name=name, due_by=due_by, notes=notes, user=request.user)
            a.save()
            return HttpResponseRedirect(request.path)
        
        return HttpResponseRedirect(request.path)