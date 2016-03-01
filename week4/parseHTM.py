import re
import urllib

def print_href_recursive(link, N, limitN):
    hand = urllib.urlopen(link)
    for line in hand:
        sublinkList = re.findall('"(http.+?)"', line)
        if len(sublinkList)>0:
            for sublink in sublinkList:
                print sublink
                if N+1 < limitN:
                    print_href_recursive(sublink, N+1, limitN)
    hand.close()

print_href_recursive('http://www.dr-chuck.com', 0, 2)
