import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a') # look for 'a' tag, tags is a list of BeautifulSoup tag.

for tag in tags:
    print tag.get('type', None)
