from bs4 import BeautifulSoup
#from operator import itemgetter
#import requests
import urllib2
import datetime
import os
from readuser import read_user

user = read_user(0)

user_seq = user['1'][0]
user_name = user['1'][1]
user_profit = user['1'][2]
user_email = user['1'][3]

print "current setup is for %s, number is %s, profit target %s, email is %s" % (user_name, user_seq, user_profit, user_email)
#print type(user_email)

url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, from_encoding="utf8")


def find_value():

	d = {}

	tbody = soup.find_all('tbody')[0]
	tr_list = tbody.find_all('tr')
	print "Total Bond number is    " + str(len(tr_list))

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

result_raw = find_value()
#print result

def high_d(result_raw):

	log = open('log.html', 'w')
	line_date = str(datetime.datetime.now()) + "\n"
	log.writelines(line_date)

	high_d={}

	for key in result_raw:
		if result_raw[key] > float(user_profit):

			high_d[key] = result_raw[key]
			line_data = "Bond name: %s, Bond profit: %s;" % (key, result_raw[key]) + "\n"
			print line_data
			log.writelines(line_data)

	log.close()
	print "the total number of matched bond is", len(high_d)	
	
	return high_d

result = high_d(result_raw)

def send(result):
	if len(result) !=0:
		os.system("mail -s 'Find matched bond for you (%s) !!' %s < log.html" % (user_name, user_email))
		print "email sent!"
	else:
		print "None find!"

send(result)
