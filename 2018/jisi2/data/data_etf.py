#! /usr/bin/python
#-*- encoding: utf-8 -*-

"""
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

#print(__name__)

def etf(etf_url):
    page = urlopen(etf_url)
    soup = BeautifulSoup(page, from_encoding="utf8")

    soup = soup.p.string
    soup = eval(soup)
    #print soup
    
    rows_str = json.dumps(soup['rows'],indent=1)
    cells_list=json.loads(rows_str)
    #cells_list = cells_list[0]
    
    etf_raw ={}

    for cells in cells_list:
        etf_data = cells[u'cell']
        etf_name = etf_data[u'fund_nm'].decode('unicode_escape')
        etf_pe = etf_data[u'pe']
        etf_index_nm = etf_data[u'index_nm'].decode('unicode_escape')
        #print etf_name
        etf_raw[etf_name] = (etf_pe, etf_index_nm)
        
    etf_high = {}
    
    for i in etf_raw:
        if etf_raw[i][0] == "-" or etf_raw[i][0] == "0.000" or float(etf_raw[i][0]) <10:
            #print di[i][1]
            if etf_raw[i][1].find('金融') != -1:
                etf_high[i] = (etf_raw[i][0],etf_raw[i][1],'金融类')
            elif etf_raw[i][1].find('恒生') != -1:
                etf_high[i] = (etf_raw[i][0],etf_raw[i][1],'恒生类')
            elif etf_raw[i][0].find('0.000') != -1:
                etf_high[i] = (etf_raw[i][0],etf_raw[i][1],'NA错误类')
            elif etf_raw[i][0].find('-') != -1:
                etf_high[i] = (etf_raw[i][0],etf_raw[i][1],'NA错误类')   
            else:
                etf_high[i] = (etf_raw[i][0],etf_raw[i][1],'其他类')
                
    return etf_high

if __name__ == "__main__":
    url = 'http://jisilu.cn/jisiludata/etf.php'
    etf(url)
    
