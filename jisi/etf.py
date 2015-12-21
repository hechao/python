#! /usr/bin/python
#-*- encoding: utf-8 -*-

"""
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
from misc import log_a
import json

#print(__name__)

def etf(etf_url):
    page = urlopen(etf_url)
    soup = BeautifulSoup(page, from_encoding="utf8")

    p = soup.p.string
    pp = eval(p)
    
    cells = json.dumps(pp['rows'],indent=1)
    #print cells_list
    #print type(cells_list)
    cells_list=json.loads(cells)
    #print type(cells_list)
    
    di ={}

    for cell in cells_list:
        cell_dict = eval(str(cell))
        in_cell = cell_dict[u'cell']
        value_dict = eval(str(in_cell))
        #print value_dict
        cell_id = str(value_dict[u'fund_id'])
        
        #cell_name = str(value_dict[ u'index_nm'])
        cell_name = value_dict[ u'index_nm']
        cell_name = cell_name.decode('unicode_escape')
        cell_name = cell_name.encode("utf-8")
        cell_name = str(cell_name)
        #print type(cell_name)
        
        cell_pe = str(value_dict[u'pe'])
        #print cell_pe
        di[cell_name] = cell_pe
    
    #print di
        
    for i in di:
        if di[i] != "-" and di[i] != "0":
            #di_pe = str(di[i])
            if float(di[i]) <10:
                etf_line = i + "'s pe =" + di[i] + "<br>\n"
                #print etf_line
                log_a(etf_line)
        else:
                etf_line = i + "'s pe = empty value or 0" + "<br>\n"
                #print etf_line
                log_a(etf_line)
    
    return di
        
if __name__ == "__main__":
    etf()