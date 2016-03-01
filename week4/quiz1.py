import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url)
soup = BeautifulSoup(html)

tags = soup('span')

count = 0
for tag in tags:
    count = count + int(tag.contents[0])
print count
