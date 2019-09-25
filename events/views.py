from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Interview, Social, Networking, Person
# Create your views here.



class eventView(TemplateView):
    template_name = "events/events.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        interviews = Interview.objects.all()
        context['interviews'] = interviews
        networking = Networking.objects.all()
        context['networking'] = networking
        social = Social.objects.all()
        context['social'] = social
        return context