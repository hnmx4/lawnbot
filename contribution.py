import json
import urllib2

url = 'https://github.com/users/hnmx4/contributions'
res = urllib2.urlopen(url)
html = res.read()

print html
