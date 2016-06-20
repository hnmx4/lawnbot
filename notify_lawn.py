# -*- coding: utf-8 -*-

import datetime
import urllib2
from dotenv import get_key
from os.path import join, dirname

import get_contributions as gc


def denv(key):
    return get_key(join(dirname(__file__), '.env'), key)

crontable = []
outputs = []

CHANNEL_ID = denv('CHANNEL_ID')
def lawns(con):
    if con < 5:
        e_lists = { 0:':fallen_leaf:',
                    1:':seedling:',
                    2:':herb:',
                    3:':deciduous_tree:',
                    4:':cherry_blossom:'}
        return e_lists[con]
    else:
        return ':cherry_blossom:'


def say_contributions():
    url = 'https://github.com/users/' + denv('USER') + '/contributions'
    data = gc.pick_dayly_count(url)
    counts = gc.pick_dayly_count(url, 'list')
    yday = datetime.date.today() - datetime.timedelta(1)
    yday = yday.strftime('%Y-%m-%d')
    yc = int(data[yday])
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
