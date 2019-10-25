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

        try:
            month_url = int(self.request.path.split('/')[-1])
            year_url = int(self.request.path.split('/')[-2]) 
            cal = Calendar(
                year=year_url, 
                month=month_url, 
                user=self.request.user)
            if month_url == 12:
                context['next_month'] = "../{0}/{1}".format(year_url + 1, 1)
                context['prev_month'] = "../{0}/{1}".format(year_url , month_url - 1)

            elif month_url == 1:
                context['next_month'] = "../{0}/{1}".format(year_url, month_url + 1)
                context['prev_month'] = "../{0}/{1}".format(year_url - 1, 12)

            else:
                context['next_month'] = "../{0}/{1}".format(year_url, month_url + 1)
                context['prev_month'] = "../{0}/{1}".format(year_url, month_url - 1)

        except:
            cal = Calendar(year=d.year, month=d.month, user=self.request.user)
            if d.month == 1:
                context['next_month'] = "{0}/{1}".format(d.year, d.month + 1)
                context['prev_month'] = "{0}/{1}".format(d.year - 1, 12) 
            if d.month == 12:
                context['next_month'] = "{0}/{1}".format(d.year + 1, 1)
                context['prev_month'] = "{0}/{1}".format(d.year, d.month - 1)
            else:
                context['next_month'] = "{0}/{1}".format(d.year, d.month + 1)
                context['prev_month'] = "{0}/{1}".format(d.year, d.month - 1)


        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        
        return context

    def post(self, request, *args, **kwargs):
        form = self.GoogleCalendarForm(request.POST)
        if form.is_valid():
            choice = form['yes_no'].value()
            if choice == 'Yes':
                if self.request.user.id == None:
                    return HttpResponse("<script> window.confirm('You must log in to connect to your Google Calendar!');"+
                    "window.location.href = '../tasks' </script>") 
                get_events(request.user)
                return HttpResponseRedirect('../calendar')
            if choice == 'No':
                return HttpResponseRedirect('../calendar')


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()