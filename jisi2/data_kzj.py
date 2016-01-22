#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
#import sys  

#reload(sys)  
#sys.setdefaultencoding('utf8')

def kzj(kzj_url, price):
    page = urlopen(kzj_url)
    soup = BeautifulSoup(page, from_encoding="utf8")
    soup = soup.p.text
    null =''
    soup = eval(soup)

    rows_str = json.dumps(soup['rows'],indent=1)
    #print type(rows)
    cells_lst=json.loads(rows_str)
    
    kzj_pick ={}
    
    for cells in cells_lst:
        kzj_data = cells[u'cell']
        #print kzj_data
        kzj_name = kzj_data[u'bond_nm'].decode('unicode_escape')
        #print fj_name
        kzj_discount = kzj_data[u'price']
        kzj_discount = float(kzj_discount[:-1])
        if kzj_discount <= price:
            #print fj_discount
            kzj_pick[kzj_name] = kzj_discount
    #print kzj_pick
    return kzj_pick
        
if __name__ == "__main__":
    kzj_url = 'http://www.jisilu.cn/data/cbnew_ajax/get_aqd_cb_list/'
    kzj(kzj_url)
    