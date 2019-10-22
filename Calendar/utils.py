from datetime import datetime, timedelta
from calendar import HTMLCalendar
from Tasks.models import *
from events.models import *
from itertools import chain

class CalendarObject:
    def __init__(self,model, color):
        self.model = model
        self.color = color

class Calendar(HTMLCalendar):
    def __init__(self, user,year=None, month=None):
        self.year = year
        self.user = user
        self.month = month
        
        super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
    def formatday(self, day, events):
        events_per_day = [] 
        for i in events:
            try:
                if i.model.start_time.day == day:
                    events_per_day.append(i)
            except:
                if i.model.due_by.day == day:
                    events_per_day.append(i)

        d = ''

        for event in events_per_day:
            if event.color == 'rgb(14, 9, 58)' or event.color == 'rgb(29, 51, 31)'  :
                d += (f'<a href="../events"><li style="background-color:{event.color};' +
                f'margin-bottom:4px; list-style-type:none;">' +
                f'{event.model.company} @ {str(event.model.start_time)[-14:-9]} </li></a>')

            elif event.color == 'rgb(80, 5, 5)':
                d += (f'<a href="../tasks"><li style="background-color:{event.color};' +
                f'margin-bottom:4px; list-style-type:none;">' + 
                f'{event.model.name} @ {str(event.model.due_by)[-14:-9]} </li></a>')
            
            elif event.color == 'black':
                d += (f'<a href="../tasks"><li style="background-color:{event.color};' +
                f'margin-bottom:4px; list-style-type:none;">' +
                f'{event.model.name} @ {str(event.model.start_time)[-14:-9]} </li></a>')
            
            else:
                d += (f'<a href="../tasks"><li style="background-color:{event.color};' +
                f'margin-bottom:4px; list-style-type:none;">'+
                f'{event.model.name} @ {str(event.model.due_by)[-14:-9]} </li></a>')
             
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
    def formatmonth(self, withyear=True):
        if self.user.id == None:
            self.user.id = 1 
        tasks = Task.objects.filter(due_by__year=self.year, 
        due_by__month=self.month, user__id = self.user.id)
        
        networking = Networking.objects.filter(start_time__year=self.year, 
        start_time__month =self.month, user__id = self.user.id)
        
        interviews = Interview.objects.filter(start_time__year=self.year, 
        start_time__month=self.month, user__id = self.user.id)
        
        calendar_events = []
        
        for i in interviews:
            calendar_events.append(CalendarObject(model=i, color='rgb(29, 51, 31)'))
        for i in networking:
            calendar_events.append(CalendarObject(model=i, color='rgb(14, 9, 58)'))
        for i in tasks:
            task_types = {'Other':'black', 'Exam': 'red', 'Assignment': 'rgb(80, 5, 5)', 'Coding Challenge': '#590c47'}
            calendar_events.append(CalendarObject(model=i, color=task_types[i.task_type]))

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, calendar_events)}\n'  
        return cal

