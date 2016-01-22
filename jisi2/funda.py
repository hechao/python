#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json

def funda_raw(funda_url):
    page = urlopen(funda_url)
    soup = BeautifulSoup(page, from_encoding="utf8")
    
    soup = soup.p.string # element tag, remove html
    null = ''
    soup = eval(soup)
    rows_str = json.dumps(soup['rows'],indent=1)
    funda_list=json.loads(rows_str)
    #print cells_list[0]
    #print type(cells_list)
    
    funda_raw ={}

    for cells in funda_list:
        funda_data = cells[u'cell']
        
        funda_name = funda_data[u'funda_name'].decode('unicode_escape')
        funda_discount = float(funda_data[u'funda_discount_rt'][:-1])
        funda_profit = float(funda_data[u'funda_profit_rt_next'][:-1])
        if funda_data[u'funda_base_est_dis_rt'] == '-':
            print "error to read funda_base_est_dis_rt as -, set it to -999.00"
            funda_base_profit = -999.00
        else:
            funda_base_profit = float(funda_data[u'funda_base_est_dis_rt'][:-1])
        funda_raw[funda_name] =[funda_discount, funda_profit, funda_base_profit]
    
    return funda_raw

def funda(funda_raw, discount, profit, base_profit):
    
    funda = {}
    
    for i in funda_raw:
        if funda_raw[i][0]>=discount and funda_raw[i][1]>=profit and funda_raw[i][2]<=base_profit:
            #print i
            funda[i] = funda_raw[i]
    return funda
    
if __name__ == "__main__":
    funda_url = 'http://www.jisilu.cn/data/sfnew/funda_list/'
    funda_raw = funda_raw(funda_url)
    
    funda(funda_raw, 10, 5, 0)