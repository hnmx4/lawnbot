# -*- coding: utf-8 -*-

import datetime
from dotenv import get_key
from os.path import join, dirname

import get_contributions as gc


def denv(key):
    return get_key(join(dirname(__file__), '.env'), key)


CHANNEL_ID = denv('CHANNEL_ID')
USER = denv('USER')
crontable = []
outputs = []
emoji = { 0: ':fallen_leaf:',
          1: ':seedling:',
          2: ':herb:',
          3: ':deciduous_tree:',
          4: ':cherry_blossom:'}


def say_contributions():
    level = gc.pick_dayly_level(USER)
    counts = gc.pick_dayly_count(USER, 'list')
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
