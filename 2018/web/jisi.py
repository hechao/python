#! /usr/bin/python

from bs4 import BeautifulSoup
from operator import itemgetter
import requests
import urllib2

url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, from_encoding="utf8")

def find_value():

	d = {}

	tbody = soup.find_all('tbody')[0]
	tr_list = tbody.find_all('tr')
	print "avaialbe number is    " + str(len(tr_list))

	for x in range(0, len(tr_list),1):

		name = tr_list[x].find_all('td')[0].find_all('a')[0].get('href')
		name = name[18:]
		ytm  = tr_list[x].find_all('td')[10].get('ytm')

		if len(ytm) !=0:
			value_ytm = round(float(ytm),1)
			#print value_ytm
			d[name] = value_ytm
		else:
			value_ytm = 0
			#print "ytm is 0"
			d[name] = value_ytm
	
	#d2 = sorted(d.iteritems(), key=itemgetter(1), reverse=True)
	return d

result = find_value()
#print result

for key in result:
	if result[key] >8:
		print key, result[key]

def write_log(result):
	log = open('log.html', 'w')
	log.writelines(str(result))
	log.close()

write_log(result)

