#! /usr/bin/python
#-*- encoding: utf-8 -*-

import datetime

index = '/srv/www/index.html'
etf_url = 'http://jisilu.cn/jisiludata/etf.php'
bond_url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

    
def print_html(bond_high,bond_max,etf_high):
    # open index
    log = open(index, 'w')
    log.write('<html>\n')
    log.close()
    log = open(index, 'a+')
    
    #打印head
    log.write('<head>\n')
    log.write('<title>今日PMONEY金融</title>\n')
    log.write('</head>\n')

    #打印时间
    log.write('(英文版) 本站网址是:http://42.120.16.247/<br>\n')
    log.write('<br>\n')
    log.write('生成时间'+str(datetime.datetime.now()) +'<br>\n')

    #债券打印到index
    log.write('<h3> ###以下是债券的收益信息：### </h3>\n')

    for i in bond_high:
        bond_high_log = str(i) + '的收益率是' + str(bond_high[i]) + '<br>\n'
        log.write(bond_high_log)
    log.write('<br>\n')

    log.write('最高的债券收益是：' + bond_max)

    #ETF打印到index
    log.write("<h3>###以下是ETF基金信息: ###</h3>")
    log.write("URL of ETF 网址是: " + etf_url + "<br>\n")
    log.write('<br>\n')

    for i in etf_high:
        if etf_high[i][2] == '金融类':
            etf_log = "* (%s) %s 的PE值是 %s, (对应指数 %s) <br>\n" % (etf_high[i][2], i, etf_high[i][0], etf_high[i][1])
            log.write(etf_log)
    log.write('<br>\n')

    for i in etf_high:
        if etf_high[i][2] == '恒生类':
            etf_log = "* (%s) %s 的PE值是 %s, (对应指数 %s) <br>\n" % (etf_high[i][2], i, etf_high[i][0], etf_high[i][1])
            log.write(etf_log)
    log.write('<br>\n')

    for i in etf_high:
        if etf_high[i][2] == '其他类':
            etf_log = "* (%s) %s 的PE值是 %s, (对应指数 %s) <br>\n" % (etf_high[i][2], i, etf_high[i][0], etf_high[i][1])
            log.write(etf_log)
    log.write('<br>\n')

    for i in etf_high:
        if etf_high[i][2] == 'NA错误类':
            etf_log = "* (%s) %s 的PE值是 %s, (对应指数 %s) <br>\n" % (etf_high[i][2], i, etf_high[i][0], etf_high[i][1])
            log.write(etf_log)
    log.write('<br>\n')

    log.write('<br>\n')
    log.write('</html>')
    log.close()
