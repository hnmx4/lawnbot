# -*- coding: utf-8 -*-
import datetime
import urllib2
import yaml

from dotenv import get_key
from bs4 import BeautifulSoup
from os.path import join, dirname


def denv(key):
    return get_key(join(dirname(__file__), '.env'), key)


CHANNEL_ID = denv('CHANNEL_ID')
USER = denv('USER')
CONF_FILE = join(dirname(__file__), 'conf.yml')

f = open(CONF_FILE, 'r')
config = yaml.load(f)
f.close

emoji = config['emoji']
level = config['level']
crontable = []
outputs = []


def scrap(username):
    url = 'https://github.com/users/' + username + '/contributions'
    html = urllib2.urlopen(urllib2.Request(url)).read()
    return BeautifulSoup(html, 'html.parser')


def pick_dayly_level(username, opt='dict'):
    data = {}
    counts = []
    soup = scrap(username)
    for rect in soup.find_all('rect'):
        if opt == 'dict':
            data[rect['data-date']] = level[rect['fill']]
        elif opt == 'list':
            counts.append(level[rect['fill']])

    if opt == 'dict':
        return data
    elif opt == 'list':
        return counts


def pick_dayly_count(username, opt='dict'):
    data = {}
    counts = []
    soup = scrap(username)
    for rect in soup.find_all('rect'):
        if opt == 'dict':
            data[rect['data-date']] = rect['data-count']
        elif opt == 'list':
            counts.append(rect['data-count'])

    if opt == 'dict':
        return data
    elif opt == 'list':
        return counts


def say_contributions():
    level = pick_dayly_level(USER)
    counts = pick_dayly_count(USER, 'list')
    yday = datetime.date.today() - datetime.timedelta(1)
    yday = yday.strftime('%Y-%m-%d')
    yc = int(level[yday])
    wc = 0
    for day in counts[-7:]:
        wc += int(day)

    mesg = ''
    if wc > 0:
        for i in range(0, wc):
            mesg += emoji[yc]
    else:
        mesg = ':new_moon_with_face:'

    outputs.append([CHANNEL_ID, mesg])


say_contributions()
