# -*- coding:utf-8 -*-

import sys
import json
import urllib2
from bs4 import BeautifulSoup


level = {
 '#eeeeee': 0,
 '#d6e685': 1,
 '#8cc665': 2,
 '#44a340': 3,
 '#1e6823': 4
}


def scrap(url):
  html = urllib2.urlopen(urllib2.Request(url)).read()
  return BeautifulSoup(html, 'html.parser')


def pick_dayly_level(url, opt='dict'):
  data = {}
  counts = []
  soup = scrap(url)
  for rect in soup.find_all('rect'):
    if opt == 'dict':
      data[rect['data-date']] = level[rect['fill']]
    elif opt == 'list':
      counts.append(level[rect['fill']])

  if opt == 'dict':
    return data
  elif opt == 'list':
    return counts


def pick_dayly_count(url, opt='dict'):
  data = {}
  counts = []
  soup = scrap(url)
  for rect in soup.find_all('rect'):
    if opt == 'dict':
      data[rect['data-date']] = rect['data-count']
    elif opt == 'list':
      counts.append(rect['data-count'])

  if opt == 'dict':
    return data
  elif opt == 'list':
    return counts

