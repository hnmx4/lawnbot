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
    url = 'https://github.com/users/' + get_key(dotenv_path, 'USER') + '/contributions'
    lists = gc.pick_count_list(urllib2.urlopen(urllib2.Request(url)))
    weekly = lists[-7:]
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


# def process_message(data):
#     words = ['今週'.decode('utf-8'), '草'.decode('utf-8')]
#     if data['channel'] == CHANNEL_ID:
#         flag = True
#         for word in words:
#             if data['text'].find(word) == -1:
#                 flag = False

#         if (flag):
#             outputs.append([CHANNEL_ID, lawns[pick_weekly_contributions()]])


say_contributions()
