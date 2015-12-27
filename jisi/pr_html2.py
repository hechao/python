#! /usr/bin/python
#-*- encoding: utf-8 -*-

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

fj_url = 'http://www.jisilu.cn/data/cf/cf_list/'
index = '/srv/www/index.html'

def print_part_head(part_title, description, url):
    log = open(index, 'a+')
    #打印index
    log.write('<h3> ###%s ### </h3>\n' % part_title)
    log.write('* %s<br>\n' % description)
    log.write('* 信息收集网址为: %s <br>\n' % url)
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

    return fj_str