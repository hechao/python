#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen

def bond_raw(bond_url):
    # find all the bond and relevant ytm value
	page = urlopen(bond_url)
	soup = BeautifulSoup(page, from_encoding="utf8")
	bond_raw = {}
	# find all tbody value and use 0
	tbody = soup.find_all('tbody')[0]
    # find all tr value, which is the total number of bond
	tr_list = tbody.find_all('tr')
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
	return bond_raw
    
def bond_high(bond_raw, user_profit):
# find the bond which has high profit, open log.html and write into it 
	bond_high={}
	for key in bond_raw:
		if bond_raw[key] > float(user_profit):
			bond_high[key] = bond_raw[key]
	return bond_high

def bond_max(bond_high):
#find out the max bond 
	if len(bond_high.values()) != 0:
		max_bond = max(bond_high.values())
	else:
		max_bond = 'N/A'
	max_bond = str(max_bond) + '%'
	return max_bond

