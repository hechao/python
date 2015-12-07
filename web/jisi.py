#! /usr/bin/python

import bs4 
import requests

url = 'http://www.jisilu.cn/data/bond/\#tlink_1'

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

def pr_title():
	print soup.title

def find_tbody(y):	
	tbody_all = y.find_all('tbody')[0]
	return tbody_all

def find_tr(body):
	tr_all = body.find_all('tr')
	return tr_all

tr_input = raw_input("enter: ")

tbody_result = find_tbody(soup)
tr_result = find_tr(tbody_result)

result =  tr_result[int(tr_input)]
print result

log = open('log.html', 'w')
log.writelines(str(result))
log.close()


