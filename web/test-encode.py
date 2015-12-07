#! /usr/bin/python

from bs4 import BeautifulSoup
import urllib2

url = 'http://www.jb51.net/'
page = urllib2.urlopen(url)

soup = BeautifulSoup(page,from_encoding="utf8")
print soup.original_encoding
print (soup.title).encode('gb18030')

file = open("title-test.html","w")
file.write(str(soup.title))
file.close()

 
"""
for link in soup.find_all('a'):
    print link['href']

"""
