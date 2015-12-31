#-*- encoding: utf-8 -*-
import urllib2
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

req = urllib2.Request(url = 'http://www.xueqiu.com',headers = headers)

feeddata = urllib2.urlopen(req).read()

#或者
#opener = urllib2.build_opener()

#feeddata = opener.open(request).read()

print feeddata.decode('u8')