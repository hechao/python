#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
import json
import cookielib
#import sys
#reload(sys)  
#sys.setdefaultencoding('utf8')

import cookielib, urllib2

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# default User-Agent ('Python-urllib/2.6') will *not* work
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11'),
    ]


"""stylesheets = [
    'https://www.idcourts.us/repository/css/id_style.css',
    'https://www.idcourts.us/repository/css/id_print.css',
]"""

home = opener.open('https://www.xueqiu.com')
print cj