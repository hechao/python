#! /usr/bin/python
#-*- encoding: utf-8 -*-

"""
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
#import string

#print(__name__)

def etf(etf_url):
    page = urlopen(etf_url)
    soup = BeautifulSoup(page, from_encoding="utf8")

    p = soup.p.string
    pp = eval(p)
    
    cells = json.dumps(pp['rows'],indent=1)
    cells_list=json.loads(cells)
    
    di ={}

    for cell in cells_list:
        #print cell
        cell_dict = eval(str(cell))
        in_cell = cell_dict[u'cell']
        
        value_dict = eval(str(in_cell))
        
        etf_name = value_dict[u'fund_nm']
        etf_name = etf_name.decode('unicode_escape')
        etf_name = etf_name.encode("utf-8")
        
        etf_pe = str(value_dict[u'pe'])
        
        etf_index_nm = value_dict[u'index_nm']
        etf_index_nm = etf_index_nm.decode('unicode_escape')
        etf_index_nm = etf_index_nm.encode("utf-8")
        #print etf_index_nm
        
        di[etf_name] = (etf_pe, etf_index_nm)

        #print di
        
    high_di = {}
    
    for i in di:
        if di[i][0] == "-" or di[i][0] == "0.000" or float(di[i][0]) <10:
            #print di[i][0]
            high_di[i] = (di[i][0],di[i][1])
                
    #print high_di
    return high_di

if __name__ == "__main__":
    url = 'http://jisilu.cn/jisiludata/etf.php'
    etf(url)
    
