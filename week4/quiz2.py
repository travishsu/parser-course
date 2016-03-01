import urllib
from BeautifulSoup import *

count    = 7
position = 18
url = raw_input('Enter URL: ')

for iter in range(count):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print url

print tags[position-1].contents[0]
