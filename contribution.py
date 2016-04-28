import sys
import json
import urllib.request

from xml.dom import minidom
from json import dumps
from bs4 import BeautifulSoup


def convert_svg_file_to_json(svg_file, elements):
  dicts = []
  svg = svg_file.read()
  soup = bs4(svg, selfClosingTags=['defs', 'sodipodi:namedview'])
  for path in soup.findAll('path'):
    path_dict = {k:path[k] for k in elements if k in dict(path.attrs)}
    if len(path_dict) > 0:
      dicts.append(path_dict)
  return dumps(dicts)


url = 'https://github.com/users/hnmx4/contributions'
res = urllib.request.urlopen(url)
html = res.read()

# convert_svg_file_to_json(html, nil)
