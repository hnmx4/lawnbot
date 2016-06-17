# -*- coding: utf-8 -*-

import time
import urllib2
import get_contributions as gc

from dotenv import get_key
from os.path import join, dirname


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
    weekly = counts[-7:]
    yesterday = int(lists[-1])

    wc = 0
    for day in weekly:
        wc += int(day)

    mesg = ''
    if wc > 0:
        for i in range(0, wc):
            mesg += lawns(yesterday)
    else:
        mesg = ':new_moon_with_face:'

    outputs.append([CHANNEL_ID, mesg])


say_contributions()
