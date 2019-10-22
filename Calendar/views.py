from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from .google_calendar import get_events
from .models import *
from .utils import Calendar
from .forms import GoogleCalendarForm
class CalendarView(generic.ListView):
    
    model = GoogleCalendar
    template_name = 'Calendar/calendar.html'
    GoogleCalendarForm = GoogleCalendarForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(year=d.year, month=d.month, user=self.request.user)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

    def post(self, request, *args, **kwargs):
        form = self.GoogleCalendarForm(request.POST)
        if form.is_valid():
            choice = form['yes_no'].value()
            if choice == 'Yes':
                get_events(request.user)
                return HttpResponseRedirect('../calendar')
            if choice == 'No':
                return HttpResponseRedirect('../calendar')


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()