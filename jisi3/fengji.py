#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json

#fj_url = 'http://www.jisilu.cn/data/cf/cf_list/'

def fj(fj_url, discount):
    page = urlopen(fj_url)
    soup = BeautifulSoup(page, from_encoding="utf8")
    soup = soup.p.text
    null =''
    soup = eval(soup)

    rows_str = json.dumps(soup['rows'],indent=1)
    #print type(rows)
    cells_lst=json.loads(rows_str)
    
    fj_pick ={}
    
    for cells in cells_lst:
        fj_data = cells[u'cell']
        fj_name = fj_data[u'fund_nm'].decode('unicode_escape')
        #print fj_name
        fj_discount = fj_data[ u'discount_rt']
        fj_discount = float(fj_discount[:-1])
        if fj_discount >= discount:
            #print fj_discount
            fj_pick[fj_name] = fj_discount
    #print fj_pick
    return fj_pick
    
        
if __name__ == "__main__":
    fj_url = 'http://www.jisilu.cn/data/cf/cf_list/'
    fj(fj_url)
    