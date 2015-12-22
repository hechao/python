#! /usr/bin/python
#-*- encoding: utf-8 -*-

from datetime import datetime
import indice

index = '/srv/www/index.html'
etf_url = 'http://jisilu.cn/jisiludata/etf.php'
bond_url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

fj_url = 'http://www.jisilu.cn/data/cf/cf_list/'
kzj_url = 'http://www.jisilu.cn/data/cbnew_ajax/get_aqd_cb_list/'

def print_html(bond_high,bond_max,etf_high, fj, kzj):
    # open index
    log = open(index, 'w')
    log.write('<html>\n')
    log.close()
    log = open(index, 'a+')
    
    #打印head
    log.write('<head>\n')
    log.write('<title>今日PMONEY金融,订阅客户:hechao!</title>\n')
    log.write('</head>\n')

    #打印时间
    log.write('<h3>今日PMONEY金融,订阅客户:hechao!</h3>\n')
    log.write('(英文版) 本站网址是:http://42.120.16.247/<br>\n')
    log.write('<br>\n')
    log.write('生成时间'+str(datetime.now()) +'<br>\n')

    #债券打印到index
    log.write('<h3> ###以下是债券的收益信息：### </h3>\n')
    log.write('程序自动抓取隐含收益在9%以上的债券信息.<br>\n')
    log.write('信息收集网址为:' +bond_url+'<br>\n')
    log.write('<br>\n')
    
    for i in bond_high:
        bond_high_log = str(i) + '的收益率是 ' + str(bond_high[i]) + '%<br>\n'
        log.write(bond_high_log)
    log.write('<br>\n')

    log.write('最高的债券收益是：' + bond_max)

    #ETF打印到index
    log.write("<h3>###以下是ETF基金信息: ###</h3>")
    log.write('程序自动抓取PE在10以下的ETF信息.<br>\n')
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
    
    #打印封基到index
    log.write('<h3> ###以下是传统封基的收益信息：### </h3>\n')
    log.write('程序自动抓取折价在15%以上的传统封基的信息.<br>\n')
    log.write('信息收集网址为:' +fj_url+'<br>\n')
    log.write('<br>\n')

    for i in fj:
        fj_line = " %s 的折价率是 %s <br>\n" % (i, fj[i])
        log.write(fj_line)
        
    #打印可转债到index
    log.write('<h3> ###以下是可转债的收益信息：### </h3>\n')
    log.write('程序自动抓取价格在100以下的可转债的信息.<br>\n')
    log.write('信息收集网址为:' +kzj_url+'<br>\n')
    log.write('<br>\n')

    for i in kzj:
        kzj_line = " %s 的现价是 %s <br>\n" % (i, kzj[i])
        log.write(kzj_line)

def print_indice_head():
    log = open(index, 'a+')
    #打印index
    log.write('<h3> ###以下是指数收集信息：### </h3>\n')
    
def print_indice(nm):
    log = open(index, 'a+')

    gain = indice.in_gain(nm)
    gain_line1 = format(gain[0], '.2%')
    gain_line2 = format(gain[1], '.2%')
    gain_line3 = format(gain[2], '.2%')
    gain_line = '%s 近期收益 一天:%s, 三天:%s, 七天:%s' % (nm, gain_line1, gain_line2, gain_line3)
    #print type(gain_line)
    log.write(gain_line)
    log.write('<br>\n')

def html_end():
    log = open(index, 'a+')
    log.write('</html>')
    log.close()