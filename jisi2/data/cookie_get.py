#! /usr/bin/python
#-*- encoding: utf-8 -*-

import cookielib, urllib2

def content(index_url):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # default User-Agent ('Python-urllib/2.6') will *not* work
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'),
        ]
    #open homepage first to get cookie, and then open target URL again to get the target content
    home = opener.open('http://xueqiu.com')
    quote = opener.open(index_url)
    content = quote.read()
    return content