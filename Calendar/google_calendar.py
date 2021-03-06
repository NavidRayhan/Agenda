import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.http import HttpResponseRedirect
from Tasks.models import Task
from events.models import Interview
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_events(user):
    creds = None
    path = os.path.abspath('client_secret_911162810929-pev52f68vgov9h4sk4iapota327j8ua7.apps.googleusercontent.com.json')
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if user.id == 1:
        if os.path.exists('token_navid.pickle'):
            with open('token_navid.pickle', 'rb') as token:
                creds = pickle.load(token)
    #  If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        #with open('token.pickle', 'wb') as token:
        #    pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=50, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        if (len(Interview.objects.filter(user=user , 
                                company=event['summary'], 
                                location=event['location'],
                                notes=event['description'], 
                                start_time  =event['start']['dateTime'])) == 0):
            
            people = ""
            print("HIHII")
            print(event['attendees'])
            for i in event['attendees'][0]:
              if i=='email' and event['attendees'][0]['self'] != True:
                print("YEEEE")
                people += event['attendees'][0][i] + ", "
            a = Interview(
              user=user, 
              company=event['summary'], 
              location=event['location'],
              notes=event['description'],
              start_time=event['start']['dateTime'],
              end_time= event['end']['dateTime'],
              people=people
              )
            a.save()


    event = {
      'summary': 'TEST EVENTS 1 ',
      'location': '800 Howard St., San Francisco, CA 94103',
      'description': 'A chance to hear more about Google\'s developer products.',
      'start': {
        'dateTime': '2019-11-28T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': '2019-11-28T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=2'
      ],
      'attendees': [
        {'email': 'lpage@example.com'},
        {'email': 'sbrin@example.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    #event = service.events().insert(calendarId='primary', body=event).execute()
    print('Done')
    HttpResponseRedirect('../calendar')
