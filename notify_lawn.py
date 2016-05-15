import time
import urllib2
import get_contributions as gc

from dotenv import get_key
from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')

crontable = []
outputs = []

crontable.append([86400, 'say_count_contributions'])

def say_count_contributions():
    lists = gc.pick_count_list(urllib2.urlopen(urllib2.Request(get_key(dotenv_path, 'URL'))))
    weekly = lists[-7:]

    weekly_contributions = 0
    for day in weekly:
        weekly_contributions += int(day)

    outputs.append([get_key(dotenv_path, 'CHANNEL_ID'), "weekly contributions: " + str(weekly_contributions)])
