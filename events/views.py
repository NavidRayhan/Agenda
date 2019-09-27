from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Interview, Social, Networking, Person
from .forms import InterviewForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.



class eventView(TemplateView):
    
    model = Interview
    template_name = "events/events.html"
    form_class = InterviewForm

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
        form = self.form_class(request.POST)
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