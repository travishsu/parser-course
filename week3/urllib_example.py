import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

word_count = dict()
for line in fhand:
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
print word_count
