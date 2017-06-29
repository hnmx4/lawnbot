# -*- coding: utf-8 -*-
import datetime
import urllib3
import certifi
import yaml

from dotenv import load_dotenv
from bs4 import BeautifulSoup
from os import environ
from os.path import join, dirname
from rtmbot.core import Plugin


class Notification(Plugin):
    load_dotenv(join(dirname(__file__), '.env'))

    def configure(self):
        f = open(join(dirname(__file__), 'conf.yml'), 'r')
        config = yaml.load(f)
        f.close()
        return config

    def scrap(self, username):
        url = 'https://github.com/users/' + username + '/contributions'
        http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',  # Force certificate check.
            ca_certs=certifi.where(),  # Path to the Certifi bundle.
        )
        r = http.request('GET', url)
        html = r.data
        return BeautifulSoup(html, 'html.parser')

    def pick_dayly_level(self, username, opt='dict'):
        config = self.configure()
        level = config['level']

        data = {}
        counts = []
        soup = self.scrap(username)
        for rect in soup.find_all('rect'):
            if opt == 'dict':
                data[rect['data-date']] = level[rect['fill']]
            elif opt == 'list':
                counts.append(level[rect['fill']])

        if opt == 'dict':
            return data
        elif opt == 'list':
            return counts

    def pick_dayly_count(self, username, opt='dict'):
        data = {}
        counts = []
        soup = self.scrap(username)
        for rect in soup.find_all('rect'):
            if opt == 'dict':
                data[rect['data-date']] = rect['data-count']
            elif opt == 'list':
                counts.append(rect['data-count'])

        if opt == 'dict':
            return data
        elif opt == 'list':
            return counts

    def process_message(self, data):
        config = self.configure()
        emoji = config['emoji']
        user = environ.get('GITHUB_USERNAME')

        level = self.pick_dayly_level(user)
        counts = self.pick_dayly_count(user, 'list')
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

        self.outputs.append([environ.get('CHANNEL_ID'), mesg])
