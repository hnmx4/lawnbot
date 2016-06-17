# -*- coding:utf-8 -*-

import sys
import json
import urllib2
from bs4 import BeautifulSoup


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
