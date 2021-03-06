#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
from datetime import datetime
import socket

class MyException(Exception):
    pass
    
def indice():
    indice_dt = {}
    indice_dt['INX:IOM'] = ['Americas', 'S&P 500'];
    indice_dt['COMP:NAS'] = ['Americas', 'NASDAQ Composite'];
    indice_dt['DJI:DJI'] = ['Americas', 'Dow Jones Industrial Average'];
    indice_dt['AW01:FSI'] = ['Americas', 'FTSE All-World $'];
    
    indice_dt['FTPP:FSI'] = ['Europe','FTSE Eurofirst 300'];
    indice_dt['FTSE:FSI'] = ['Europe','FTSE 100'];
    indice_dt['CAC:PAR'] = ['Europe','CAC 40'];
    indice_dt['DAXX:GER'] = ['Europe','Xetra DAX'];
    
    indice_dt['n225:NIK'] = ['Asia-Pacifi','Nikkei 225'];
    indice_dt['HSI:HKG'] = ['Asia-Pacifi','Hang Seng'];
    indice_dt['XJO:ASX'] = ['Asia-Pacifi','S&P/ASX 200'];
    indice_dt['SHI:SHH'] = ['Asia-Pacifi','Shanghai Composite'];
    indice_dt['IXJ:TYO'] = ['Asia-Pacifi','Topix'];
    
    indice_dt_update = indice_dt
    
    for i in indice_dt_update:
        #print i, indice_dt[i]
        indice_url ='http://markets.ft.com/research/Markets/Tearsheets/Summary?s=%s' % i
        print indice_url
        while True:
            try:
                page = urllib2.urlopen(indice_url, timeout=10)
                soup = BeautifulSoup(page, from_encoding="utf8")
            except urllib2.URLError:
                print "Bad URL!"
                #indice_dt_update[i].append('Data Read Bad URL!')
                #indice_dt_update[i].append('Data Read Bad URL!')
                continue
                #print type(e)
                #raise MyException("There was an error: %r" % e)
        
            except socket.timeout:
                print "Timeout!"
                #indice_dt_update[i].insert(1, 'Data Read Timeout!')
                #indice_dt_update[i].insert(2, 'Data Read Timeout!')
                continue
            
            break
            
        indice_close = soup.find_all("tr", "last")[1].find_all('td')[0]
        #print indice_close
        indice_close = indice_close.string.encode('utf-8')
        indice_close = indice_close.replace(",", "")
        indice_dt_update[i].insert(2, indice_close)
            
        indice_indicator = soup.find_all("div", "indicator")[0].get('style')
        #print indice_indicator
        indice_dt_update[i].insert(3, indice_indicator)
        #print indice_dt_update[i]
    
    #print indice_dt_update
    return indice_dt_update

if __name__ == "__main__":
    #indice_nm = 'SHI:SHH'
    #indice_dt = indice_dt()
    indice()