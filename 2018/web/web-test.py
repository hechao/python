#! /usr/bin/python

import urllib2

url = raw_input("paste the url:   ")    
req = urllib2.Request(url)    
response = urllib2.urlopen(req)    
the_page = response.read()    
print the_page  
