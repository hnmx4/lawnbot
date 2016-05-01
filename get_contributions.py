import sys
import json
import urllib.request

from bs4 import BeautifulSoup


def pick_count_list(res):
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


url = 'https://github.com/users/hnmx4/contributions'
res = urllib.request.urlopen(url)

lists = pick_count_list(res)
print(lists)
