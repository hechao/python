#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json

def stock(stock_url, month):
    page = urlopen(stock_url)
    soup = BeautifulSoup(page, from_encoding="utf8")
    soup = soup.p.text
    null =''
    soup = eval(soup)
    
    #print soup

    rows_str = json.dumps(soup['rows'],indent=1)
    #print rows_str
    cells_lst=json.loads(rows_str)
    stock_pick ={}
    month_n = 0
    month_p = 0
    if month == 12:
            month_n = 01
            month_p = 11
    elif month == 01:
            month_n = 02
            month_p = 12
    else:
        month_n = month
        month_p = month
    
    stk_great = '\u5f3a\u70c8\u5efa\u8bae'
    stk_good = '\u5efa\u8bae\u7533\u8d2d'
    
    count = 0
    for cell in cells_lst:
        stock_data = cell[u'cell']
        stock_nm = stock_data[u'stock_nm'].decode('unicode_escape')
        stock_advise = stock_data[ u'jsl_advise']
        apply_dt = stock_data[u'apply_dt'].decode('unicode_escape')
        apy_months = int(apply_dt[0:2])
        apy_days = apply_dt[3:5]
        #print apy_days
        if (stock_advise == stk_great or stock_advise == stk_great) and (apy_months == month or apy_months == month_n or apy_months == month_p) and count <=2:
            #print apply_dt
            #print stock_nm, stock_advise, apy_months, apy_days
            stock_pick[stock_nm] = [stock_advise.decode('unicode_escape'), apy_months, apy_days]
            count = count +1
    #print stock_pick
    return stock_pick
    
        
if __name__ == "__main__":
    stock_url = 'http://www.jisilu.cn/jisiludata/newstock.php?qtype=apply'
    stock(stock_url, 12)
    