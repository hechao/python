#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
import json
#import sys
#reload(sys)  
#sys.setdefaultencoding('utf8')

cookie = "s=hzi17uv5ti; bid=d11a25c82345574c16abcf288047d615_iethwirb; __utma=1.1779742401.1442737547.1445853864.1446430797.24; __utmz=1.1442738241.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); Hm_lvt_1db88642e346389874251b5a1eded6e3=1444369288,1445236220,1445579599,1446430797; xq_a_token=d63156e070445899d9ea2302789b58fa3af3d35e; xq_r_token=274e5a74fe473bb08ad4caba027c063eda1ae642"
request_headers = {
    #"GET":"HTTP/1.1",
    #"Host": "xueqiu.com",
    #"Connection": "keep-alive",
    #"Cache-Control": "max-age=0",
    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #"Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    #"Referer": "http://xueqiu.com/7712974144",
    #"Accept-Encoding": "gzip, deflate, sdch",
    #"Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    #'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    #"Cookie": cookie,
    }

def index(index_url):
    request = Request(index_url, headers=request_headers)
    page = urlopen(request).read()
    soup = BeautifulSoup(page, from_encoding="utf8")

    soup = soup.p.string
    soup = eval(soup)
    #print soup
    #print type(soup)
    
    dumps = json.dumps(soup,indent=1)
    index=json.loads(dumps)
    #index = index_loads
    #print index
    index_raw ={}

    for index_each in index:
        #print index_each
        index_id = index[index_each][u'code']
        index_nm = index[index_each][u'name']#.decode('unicode_escape'))
        index_value = index[index_each][u'current']
        index_change = index[index_each][u'percentage']
        index_raw[index_id] = [index_nm, index_value, index_change]
    
    return index_raw

if __name__ == "__main__":
    index_url = 'http://xueqiu.com/v4/stock/quote.json?code=SH000001%2CSZ399001%2CHKHSI%2CDJI30'
    index(index_url)