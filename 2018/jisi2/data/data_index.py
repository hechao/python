#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2, json, cookielib
from cookie_get import content

"""cookie = "s=hzi17uv5ti; bid=d11a25c82345574c16abcf288047d615_iethwirb; _sid=aeHts7g2HICu1YqFj3gakImvYqNhRR; xq_a_token=c0a8781567fa9bf50062eb18298c8b0176f0b9e9; xqat=c0a8781567fa9bf50062eb18298c8b0176f0b9e9; xq_r_token=2d7cd99fb375796ffff8caae27a11e3ae4b972d5; xq_is_login=1; u=7712974144; xq_token_expire=Mon%20Jan%2025%202016%2016%3A25%3A00%20GMT%2B0800%20(CST); Hm_lvt_1db88642e346389874251b5a1eded6e3=1451550295; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1451557584; __utmt=1; __utma=1.1779742401.1442737547.1451554654.1451556504.27; __utmb=1.2.10.1451556504; __utmc=1; __utmz=1.1442738241.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    "Cookie": cookie,
    }"""

def index(index_url):
    #request = urllib2.Request(index_url, headers=request_headers)
    page = content(index_url)
    soup = BeautifulSoup(page, from_encoding="utf8")

    soup = soup.p.string
    soup = eval(soup)
    
    dumps = json.dumps(soup,indent=1)
    index=json.loads(dumps)

    index_raw ={}

    for index_each in index:
        #print index_each
        index_id = index[index_each][u'code']
        index_nm = index[index_each][u'name']#.decode('unicode_escape'))
        index_value = index[index_each][u'current']
        index_change = index[index_each][u'percentage']
        index_raw[index_id] = [index_nm, index_value, index_change]
    
    #print index_raw
    return index_raw

if __name__ == "__main__":
    index_url = 'http://xueqiu.com/v4/stock/quote.json?code=SH000001%2CSZ399001%2CHKHSI%2CDJI30'
    index(index_url)