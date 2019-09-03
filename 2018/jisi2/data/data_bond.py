#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen

def bond_raw(bond_url):
    # find all the bond and relevant ytm value
	page = urlopen(bond_url)
	soup = BeautifulSoup(page, from_encoding="utf8")
	bond_raw = {}

	bond_name_list = soup.find_all("td", "acenter nowrap")
	bond_value_rawlist = soup.find_all("td", ytm=True)
	bond_value_list = []
	for i in bond_value_rawlist:
	    i = i.get('ytm')
	    '''if i != "":
	        print "error read bond ytm as ' ', set it to -999"
	        i = -999.00
	        bond_value_list.append(i)
	    else:'''
	    bond_value_list.append(i)
	       
	bond_value_list = bond_value_list[1::2]
	#print bond_value_list
	for i in range(len(bond_name_list)):
	    bond_name = bond_name_list[i].string
	    bond_value = bond_value_list[i]
	    bond_raw[bond_name] = bond_value
	    #print type(bond_value)
	    
	#print bond_raw
	return bond_raw
    
def bond_high(bond_raw, user_profit):
# find the bond which has high profit, open log.html and write into it 
	bond_high={}
	for key in bond_raw:
	    #print bond_raw[key]
	    if float(bond_raw[key]) > float(user_profit):
	        print 'high bond value: ' + bond_raw[key]
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

if __name__ == "__main__":
    bond_url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

    bond_raw = bond_raw(bond_url)
    bond_high = bond_high(bond_raw, 9)
    #print bond_high
    bond_max = bond_max(bond_high)
