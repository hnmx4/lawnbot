# -*- coding: utf-8 -*-

import time
import urllib2
import get_contributions as gc

from dotenv import get_key
from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')

crontable = []
outputs = []

CHANNEL_ID = get_key(dotenv_path, 'CHANNEL_ID')
lawns = { 0:':new_moon_with_face:',
          1:':seedling:',
          2:':herb:',
          3:':deciduous_tree:',
          4:':cherry_blossom:'}


def pick_weekly_contributions():
    url = 'https://github.com/users/' + get_key(dotenv_path, 'USER') + '/contributions'
    lists = gc.pick_count_list(urllib2.urlopen(urllib2.Request(url)))
    weekly = lists[-7:]

    weekly_contributions = 0
    for day in weekly:
        weekly_contributions += int(day)

    return weekly_contributions


def say_weekly_contributions():
    outputs.append([CHANNEL_ID, lawns[pick_weekly_contributions()]])


def process_message(data):
    words = ['今週'.decode('utf-8'), '草'.decode('utf-8')]
    if data['channel'] == CHANNEL_ID:
        flag = True
        for word in words:
            if data['text'].find(word) == -1:
                flag = False

        if (flag):
            outputs.append([CHANNEL_ID, lawns[pick_weekly_contributions()]])


say_weekly_contributions()
