import sys
import json
import urllib.request

from bs4 import BeautifulSoup


def pick_count_w_date_list(res):
  lists = []
  dict_obj = {}
  html = res.read()
  soup = BeautifulSoup(html, 'html.parser')
  for rect in soup.find_all('rect'):
    dict_obj = {
      'data-date'  : rect['data-date'],
      'data-count' : rect['data-count']
      }
    lists.append(dict_obj)
  return lists


def pick_count_list(res):
  lists = []
  html = res.read()
  soup = BeautifulSoup(html, 'html.parser')
  for rect in soup.find_all('rect'):
    lists.append(rect['data-count'])
  return lists


url = 'https://github.com/users/hnmx4/contributions'
lists = pick_count_list(urllib.request.urlopen(url))
weekly = lists[-7:]

weekly_contributions = 0
for day in weekly:
  weekly_contributions += int(day)

print(weekly_contributions)
