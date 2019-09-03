#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
from datetime import datetime


def indice(indice_nm):
	# find all the bond and relevant ytm value
	indice_url ='http://markets.ft.com/research//Tearsheets/PriceHistoryPopup?symbol=%s' % indice_nm
	
	page = urlopen(indice_url)
	soup = BeautifulSoup(page, from_encoding="utf8")
	bond_raw = {}
	tbody = soup.find_all('tbody')[0]
	tr_list = tbody.find_all('tr')
	in_d = {}
        a = 0
	for tr in tr_list:

	    td = tr.find_all('td')
	    date = td[1].string
	    date = date.encode('utf-8')

	    close_value = td[5].string
	    close_value = close_value.encode('utf-8')
	    close_value = float(close_value.replace(",", ""))
	    in_d[a] = (date, close_value)
	    a = a+1
	
	return in_d

def in_gain(indice_nm):
    in_d = indice(indice_nm)
    x1 = (in_d[0][1]-in_d[1][1])/in_d[0][1]
    x3 = (in_d[0][1]-in_d[3][1])/in_d[0][1]
    x7 = (in_d[0][1]-in_d[8][1])/in_d[0][1]
    gain =(x1, x3, x7)
    return gain
    
if __name__ == "__main__":
    indice_nm = 'SHI:SHH'
    in_gain(indice_nm)

