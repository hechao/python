"""
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
from misc import log
import json

print(__name__)

def etf():
    url = 'http://jisilu.cn/jisiludata/etf.php'

    page = urlopen(url)
    soup = BeautifulSoup(page, from_encoding="utf8")

    p = soup.p.string
    d = eval(p)
    
    cells = json.dumps(d['rows'],indent=1)
    #print cells_list
    #print type(cells_list)
    cells_list=json.loads(cells)
    print type(cells_list)
    
    di ={}

    for cell in cells_list:
        cell_dict = eval(str(cell))
        in_cell = cell_dict[u'cell']
        value_dict = eval(str(in_cell))
        #print value_dict
        cell_id = str(value_dict[u'fund_id'])
        #print cell_id
        cell_pe = str(value_dict[u'pe'])
        #print cell_pe
        di[cell_id] = cell_pe
        
    for i in di: 
        print i, "'s pe =", di[i]
        
if __name__ == "__main__":
    etf()