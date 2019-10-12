from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Interview, Social, Networking, Person
from .forms import InterviewForm, DeleteForm
from django.http import HttpResponseRedirect, HttpResponse
import datetime



# Create your views here.



class eventView(TemplateView):
    
    DeleteForm = DeleteForm
    InterviewForm = InterviewForm
    model = Interview
    template_name = "events/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        interviews = Interview.objects.all()
        context['interviews'] = interviews
        context['interviews']
        networking = Networking.objects.all()
        context['networking'] = networking
        social = Social.objects.all()
        context['social'] = social
        return context
    
    def post(self, request, *args, **kwargs):
        try:
            form = self.InterviewForm(request.POST)
            company = form['company'].value()
            location = form['location'].value()
            start_time = form['start_time'].value()
            end_time = form['end_time'].value()
            notes = form['notes'].value()
            a = Interview(company=company,
                    location=location,
                    start_time=start_time,
                    end_time = end_time,
                    notes= notes)
            a.save()
            return HttpResponseRedirect(request.path)

        except:
            form = self.DeleteForm(request.POST)
            company= form['company'].value()
            start_time = form['start_time'].value()
            #d = datetime.datetime.strptime(start_time)
            d = start_time.format("YYYY-MM-DD[T]HH:mm:ss")
            print(d) # or print(str(d)) if you want it as a string 

            print(Interview.objects.all().filter(company=company))
            print(start_time)
            Interview.objects.all().filter(company=company, start_time__gte=start_time,
            start_time__lte=start_time+":59+00:00").delete()
            return HttpResponseRedirect(request.path)

        