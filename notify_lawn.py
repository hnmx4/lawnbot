# -*- coding: utf-8 -*-

import datetime
from dotenv import get_key
import urllib2
from os.path import join, dirname
from bs4 import BeautifulSoup

def denv(key):
    return get_key(join(dirname(__file__), '.env'), key)


crontable = []
outputs = []

CHANNEL_ID = denv('CHANNEL_ID')


def pick_dayly_count(url, opt='dict'):
    res = urllib2.urlopen(urllib2.Request(url))
    data = {}
    counts = []
    html = res.read()
    soup = BeautifulSoup(html, 'html.parser')
    for rect in soup.find_all('rect'):
        if opt == 'dict':
            data[rect['data-date']] = rect['data-count']
        elif opt == 'list':
            counts.append(rect['data-count'])

    if opt == 'dict':
        return data
    elif opt == 'list':
        return counts


def lawns(con):
    if con < 5:
        e_lists = {
            0: ':fallen_leaf:',
            1: ':seedling:',
            2: ':herb:',
            3: ':deciduous_tree:',
            4: ':cherry_blossom:'
        }
        return e_lists[con]
    else:
        return ':cherry_blossom:'


def say_contributions():
    url = 'https://github.com/users/' + denv('USER') + '/contributions'
    data = pick_dayly_count(url)
    counts = pick_dayly_count(url, 'list')
    yday = datetime.date.today() - datetime.timedelta(1)
    yday = yday.strftime('%Y-%m-%d')
    yc = data[yday]
    wc = 0
    for day in counts[-7:]:
        wc += int(day)

    mesg = ''
    if wc > 0:
        for i in range(0, wc):
            mesg += lawns(yc)
    else:
        mesg = ':new_moon_with_face:'

    outputs.append([CHANNEL_ID, mesg])


say_contributions()
