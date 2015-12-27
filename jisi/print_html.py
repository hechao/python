#! /usr/bin/python
#-*- encoding: utf-8 -*-

from datetime import datetime
#import world_indice
#import indice

index = '/srv/www/index.html'
etf_url = 'http://jisilu.cn/jisiludata/etf.php'
bond_url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

fj_url = 'http://www.jisilu.cn/data/cf/cf_list/'
kzj_url = 'http://www.jisilu.cn/data/cbnew_ajax/get_aqd_cb_list/'
indice_url = 'www.ft.com'
funda_url = 'http://www.jisilu.cn/data/sfnew/funda_list/'

def html_head():
    # open index
    log = open(index, 'w')
    
    log.write('<!DOCTYPE html>')
    log.close()
    log = open(index, 'a+')
    
    #打印html
    log.write('<html>\n')
    #打印head
    log.write('<head>\n')
    log.write('<meta content="text/html;charset=utf-8" http-equiv="Content-Type" />\n')
    log.write('<title>今日PMONEY金融,订阅客户:hechao!</title>\n')
    log.write('</head>\n')

    #打印时间
    log.write('<h3>今日PMONEY金融,订阅客户:hechao!</h3>\n')
    
    log.write('* 有些投资机会和窗口转瞬即逝, 抓住机会，轮动收益')
    log.write('* (英文版) 本站网址是:http://42.120.16.247/<br>\n')
    log.write(datetime.now().strftime('* 生成时间: %y-%m-%d %I:%M:%S %p <br>\n'))
 
def print_part_head(part_title, description, url):
    log = open(index, 'a+')
    #打印index
    log.write('<h3> ###%s ### </h3>\n' % part_title)
    log.write('* %s<br>\n' % description)
    log.write('* 信息收集网址为: %s <br>\n' % url)
    log.write('<br>\n')
    
def html_end():
    log = open(index, 'a+')
    log.write('</html>')
    log.close()   
    
def print_bond(bond_high,bond_max):
    #债券打印到index
    print_part_head('以下是债券的收益信息:', '程序自动抓取隐含收益在9%以上的债券信息.', bond_url)
    log = open(index, 'a+')
    
    for i in bond_high:
        bond_high_log = '* %s 的收益率是 %s %%<br>\n' %(str(i), str(bond_high[i]))
        log.write(bond_high_log)
    log.write('<br>\n')

    log.write('* 最高的债券收益是：' + bond_max)

def print_etf(etf):
    print_part_head('以下是ETF基金信息:', '程序自动抓取PE在10以下的ETF信息.', etf_url)
    log = open(index, 'a+')

    for i in etf:
        if etf[i][2] == '金融类':
            etf_log = "* (%s) %s 的PE值是 %s, (对应指数 %s) <br>\n" % (etf[i][2], i, etf[i][0], etf[i][1])
            log.write(etf_log)
    log.write('<br>\n')

    for i in etf:
        if etf[i][2] == '恒生类':
            etf_log = "* (%s) %s 的PE值是 %s, (对应指数 %s) <br>\n" % (etf[i][2], i, etf[i][0], etf[i][1])
            log.write(etf_log)
    log.write('<br>\n')

    for i in etf:
        if etf[i][2] == '其他类':
            etf_log = "* (%s) %s 的PE值是 %s, (对应指数 %s) <br>\n" % (etf[i][2], i, etf[i][0], etf[i][1])
            log.write(etf_log)
    log.write('<br>\n')

    for i in etf:
        if etf[i][2] == 'NA错误类':
            etf_log = "* (%s) %s 的PE值是 %s, (对应指数 %s) <br>\n" % (etf[i][2], i, etf[i][0], etf[i][1])
            log.write(etf_log)
    log.write('<br>\n')
    
def print_fj(fj):
    #打印封基到index
    print_part_head('以下是传统封基的收益信息', '程序自动抓取折价在15%以上的传统封基的信息.', fj_url)
    log = open(index, 'a+')
    
    fj_lines =[]
    
    for i in fj:
        fj_line = " %s 的折价率是 %s <br>\n" % (i, fj[i])
        fj_lines.append(fj_line)
        fj_str = ''.join(fj_lines)
        log.write(fj_line)

    #return fj_str

def print_kzj(kzj):
    #打印可转债到index
    print_part_head('以下是可转债的收益信息', '程序自动抓取价格在100以下的可转债的信息.', kzj_url)
    log = open(index, 'a+')
    
    for i in kzj:
        kzj_line = " %s 的现价是 %s <br>\n" % (i, kzj[i])
        log.write(kzj_line)
    
def print_indice(indice_dt_update, indice_filter):
    print_part_head('以下是国际指数信息', '52K排位越低表明指数在近一年内的水准', indice_url)
    log = open(index, 'a+')
    
    for i in indice_dt_update:
        indice_line = "*** %s  类的 %s: %s  指数的值是%s,   52K排位是  %s<br>\n" % (indice_dt_update[i][0], i, indice_dt_update[i][1], indice_dt_update[i][2], indice_dt_update[i][3])
        log.write(indice_line)
    log.write('<br>\n')    

    log.write('以下过滤出52K信息在25% 的指数<br>\n')
    for i in indice_filter:
        indice_line_filter = "*** %s  类的 %s: %s  指数的值是%s,   52K排位是  %s%%<br>\n" % (indice_filter[i][0], i, indice_filter[i][1], indice_filter[i][2], indice_filter[i][3])
        log.write(indice_line_filter)
    
def print_funda(funda):
    print_part_head('以下是分级基金A的信息:', '提取折价率在10以下，隐含收益在5以上，母鸡溢价率在0一下的分级A.', funda_url)
    log = open(index, 'a+')
    
    for i in funda:
        funda_line = "* 分级A %s 的折价率是 %s, 隐含收益率是 %s, 母鸡溢价率是 %s. <br>\n" %(i, funda[i][0], funda[i][1], funda[i][2])
        log.write(funda_line)
    log.write('<br>\n')
