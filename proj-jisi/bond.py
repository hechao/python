from bs4 import BeautifulSoup
#from operator import itemgetter
#import requests
import urllib2
import datetime
import os

url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, from_encoding="utf8")

def find_value():
# find all the bond and relevant ytm value
	bond_raw = {}

# find all tbody value and use 0
	tbody = soup.find_all('tbody')[0]

# find all tr value, which is the total number of bond
	tr_list = tbody.find_all('tr')
	print "Total Bond number is    " + str(len(tr_list))

# find bond number in href url, and ytm value
	for x in range(0, len(tr_list),1):

		name = tr_list[x].find_all('td')[0].find_all('a')[0].get('href')
		name = name[18:]
		ytm  = tr_list[x].find_all('td')[10].get('ytm')

		if len(ytm) !=0:
			value_ytm = round(float(ytm),1)
			#print value_ytm
			bond_raw[name] = value_ytm
		else:
			value_ytm = 0
			#print "ytm is 0"
			bond_raw[name] = value_ytm
	
	#d2 = sorted(d.iteritems(), key=itemgetter(1), reverse=True)
	return bond_raw


def high_bond(bond_raw, user_profit):
# find the bond which has high profit, open log.html and write into it 
	log = open('log.html', 'w')
	line_date = str(datetime.datetime.now()) + "\n"
	log.writelines(line_date)

	high_bond={}

	for key in bond_raw:
		if bond_raw[key] > float(user_profit):

			high_bond[key] = bond_raw[key]
			line_data = "Bond name: %s, Bond profit: %s;" % (key, bond_raw[key]) + "\n"
			print line_data
			log.writelines(line_data)

	log.close()
	print "the total number of matched bond is", len(high_bond)	
	
	return high_bond


def send(result, user_name, user_email):
# send email
	if len(result) !=0:
		os.system("mail -s 'Find matched bond for you (%s) !!' %s < log.html" % (user_name, user_email))
		print "email sent!"
	else:
		print "None find!"
