#! /usr/bin/python

import bs4 
import requests

url = 'http://www.jisilu.cn/data/bond/\#tlink_1'

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

print soup.title
body = soup.find_all('tbody')[0]
#print body
tr = body.find_all('tr')
print tr[1]
