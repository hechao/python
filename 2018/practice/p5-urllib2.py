import urllib2
import sys  
from bs4 import BeautifulSoup

reload(sys)  
sys.setdefaultencoding('utf8')

request_headers = {
    "GET":"HTTP/1.1",
    "Host": "xueqiu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    "Referer": "http://xueqiu.com/7712974144",
    #"Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Cookie": "s=2wr0147fhi; webp=0; bid=d11a25c82345574c16abcf288047d615_iipn1emt; __utmt=1; snbim_minify=true; last_account=formblackt%40gmail.com; xq_a_token=a6d7b87d27b23dd623e6c9ea64007bc31ab498de; xq_r_token=b7c29adf69124dcd8d89b0152972c1b26d48f539; __utma=1.570366819.1451232583.1451287354.1451291091.4; __utmb=1.4.10.1451291091; __utmc=1; __utmz=1.1451232583.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1450543827,1450776672,1451232584; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1451291136",
    }
    
request = urllib2.Request("http://xueqiu.com", headers=request_headers)
contents = urllib2.urlopen(request).read()
soup = BeautifulSoup(contents, from_encoding="utf8")
print soup
    
    
    
    
    