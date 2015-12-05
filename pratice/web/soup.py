#! /usr/bin/python

import requests
import bs4
 
url = 'http://www.idehe.com'
 
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

x = soup.find_all('article')
print x[0]

print '----------------------------------------------'
y = x[0].find_all('a')
#print y

for num in range(0,len(y),1):
 print y[num]
