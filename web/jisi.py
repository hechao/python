#! /usr/bin/python

from bs4 import BeautifulSoup
import requests
import urllib2

url = 'http://www.jisilu.cn/data/bond/\#tlink_1'

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, from_encoding="utf8")

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



