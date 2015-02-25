#after getting all the names from the database, let's shuffle the addresses and then sort them into groups of 4 #then set events

# this runs 3-5 days BEFORE the Friday lunch -- creates 3 lunch invites (12, 12:30, 1)
import csv
import random
import sys, os
import gflags
import httplib2
import time
import datetime
import pprint
import itertools

# sys.path.append("/home/lunchbox/lunchbox")
# os.environ["DJANGO_SETTINGS_MODULE"] = "lunchboxproj.settings"
# from lunchboxapp.models import User

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

FLAGS = gflags.FLAGS

# OAUTH Stuff!
#FIXME -- new credentials
FLOW = OAuth2WebServerFlow(
    client_id='777520625445-7md8r21em7k31ukcqpb9n249ps09or4n.apps.googleusercontent.com',
    client_secret='Z-9F_50oJkyEEIDrd381rZF5',
    scope='https://www.googleapis.com/auth/calendar',
    user_agent='zenlunch/1')

# FIXME: Credentials shouldn't be hardcoded.

calendar_id = 'acoleman@zendesk.com'
developer_key = 'AIzaSyAnTzxnVYTjPlfMLpHdTooX57AM4gg-GPY'

storage = Storage('calendar.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
    credentials = run(FLOW, storage)

http = httplib2.Http()
http = credentials.authorize(http)

service = build(serviceName='calendar', version='v3', http=http,
   developerKey=developer_key)

#ACTUAL CODE BELOW!


signups = dict()

# ONLY MODIFY THESE
signups['12pm'] = ['acoleman@zendesk.com', 'acoleman@zendesk.com+1']
signups['12:30pm'] = ['angelicacoleman3@gmail.com']
signups['1:00pm'] = []
date = '2014-08-22'

# [] equivalent to list()
# {} equivalent to dict()


def random_groups(lst, n=4):
    # Randomize our new list
    random.shuffle(lst)

    # Start with an empty list of groups
    groups = []

    while lst:
        group, lst = lst[:n], lst[n:] 
        groups.append(group)
    # Return all the groups
    return groups

locations = ["Chaos", "Rainbow Shell", "Turbo", "Titan", "Sonic", "Doorman Drew",]


times = {'12pm': {'start': "%sT12:00:00.000-07:00" % date,
                  'end': "%sT12:30:00.000-07:00" % date},
         '12:30pm': {'start': "%sT12:30:00.000-07:00" % date,
                     'end': "%sT13:00:00.000-07:00" % date},
         '1:00pm': {'start': "%sT13:00:00.000-07:00" % date,
                    'end': "%sT13:30:00.000-07:00" % date}
        }
#for 'times', change date
# times = [
#      {'start': {'dateTime': '2014-08-08T12:00:00.000-07:00'},
#       'end':   {'dateTime': '2014-08-08T12:30:00.000-07:00'}},
#      {'start': {'dateTime': '2014-08-08T12:30:00.000-07:00'},
#       'end':   {'dateTime': '2014-08-08T13:00:00.000-07:00'}},
#      {'start': {'dateTime': '2014-08-08T13:00:00.000-07:00'},
#       'end':   {'dateTime': '2014-08-08T13:30:00.000-07:00'}},
#  ]

# start_times = {"12pm": '2014-08-22T12:00:00.000-07:00', "12:30pm": '2014-08-22T12:30:00.000-07:00', "1:00pm": '2014-08-22T13:00:00.000-07:00'}
# end_times = {"12:30pm":'2014-08-22T12:30:00.000-07:00', "1:00pm": '2014-08-22T13:00:00.000-07:00', "1:30pm": '2014-08-22T13:30:00.000-07:00'}

def schedule_block(block_key):
    
    groups = random_groups(signups[block_key])
    print groups
    random.shuffle(locations)

    for i, group in enumerate(groups):
        event = {
             'summary': 'LUNCHBOX LUNCH!!',
             'start': {'dateTime': times[block_key]['start']},
             'end': {'dateTime': times[block_key]['end']},
             'description': 'This is your Zendine group! Before grabbing food, meet your group at the location listed, then head to the cafe to get food and eat! The meeting location is where you meet, not where you eat.',
             'location': locations[i%len(locations)],
             'guestsCanSeeOtherGuests': True,
             'attendees': [{'email': email} for email in group],
             'reminders': {
                 'useDefault': True
             }
        }

        print event

        created_event = service.events().insert(calendarId='acoleman@zendesk.com', body=event, sendNotifications=True).execute()

        print "Created Event: %s" % created_event['id']
        print "Event Link: %s" % created_event['htmlLink']

        
for time in signups.keys():
    schedule_block(time)









