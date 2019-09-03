#! /usr/bin/python
import requests

url = raw_input("paste your url:   ")
resp = requests.get('http://'+url)
print resp.text
