from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Interview, Networking
from .forms import InterviewForm, DeleteForm, NetworkingForm
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.contrib.auth.models import User

class eventView(TemplateView):
    
    DeleteForm = DeleteForm
    InterviewForm = InterviewForm
    NetworkingForm = NetworkingForm 
    model = Interview
    template_name = "events/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("DASDSA")
        print(self.request.user.id)
        print(User.objects.all())
        try:
            interviews = Interview.objects.filter(user=self.request.user)
            context['interviews'] = interviews
            networking = Networking.objects.filter(user=self.request.user)
            context['networking'] = networking
        
        except:
            interviews = Interview.objects.filter(user=User.objects.filter(id=2)[0])
            context['interviews'] = interviews
            networking = Networking.objects.filter(user=User.objects.filter(id=2)[0])
            context['networking'] = networking
        return context

    def post(self, request, *args, **kwargs):
        if self.request.user.id == None:
            return HttpResponse("<script>alert('You must login to edit Events!'); window.location.href = '../events'; </script>") 
        form = self.InterviewForm(request.POST)
        if form.is_valid():
            company = form['company'].value()
            location = form['location'].value()
            start_time = form['start_time'].value()
            end_time = form['end_time'].value()
            notes = form['notes'].value()
            people = form['people'].value()
            a = Interview(company=company,
                    location=location,
                    people=people,
                    start_time=start_time,
                    end_time = end_time,
                    notes= notes,
                    user= self.request.user)
            a.save()
            return HttpResponseRedirect(request.path) 
        else:
            model= Networking
            form = self.NetworkingForm(request.POST)
            if form.is_valid():
                company = form['company'].value()
                location = form['location'].value()
                start_time = form['start_time'].value()
                end_time = form['end_time'].value()
                description = form['description'].value()
                roles = form['roles'].value()
                a = Networking(company=company,
                        location=location,
                        start_time=start_time,
                        end_time = end_time,
                        description= description,
                        roles= roles,
                        user= self.request.user)
                a.save()
                return HttpResponseRedirect(request.path) 

            else:
                form = self.DeleteForm(request.POST)
                if form.is_valid():
                    company= form['company'].value()
                    start_time = form['start_time'].value()
                    Interview.objects.all().filter(company=company, start_time__gte=start_time,
                    start_time__lte=start_time+":59+00:00", user=self.request.user).delete()
                    Networking.objects.all().filter(company=company, start_time__gte=start_time,
                    start_time__lte=start_time+":59+00:00", user=self.request.user).delete()    
                    return HttpResponseRedirect(request.path)
            
            return HttpResponseRedirect(request.path)    