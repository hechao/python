#! /usr/bin/python
#-*- encoding: utf-8 -*-

from misc import read_user, email
from bond import bond_raw, bond_high, bond_max
import datetime
from etf import etf
from print_html import print_html, print_indice, print_indice_head, html_end
from fj import fj
from kzj import kzj

#用户
user = read_user(0)
ID = 'hechao'
user_name = user[ID][0]
user_profit = user[ID][1]
user_email = user[ID][2]

#print "* Current user name is %s, profit target %s, email is %s" % (user_name, user_profit, user_email)

bond_url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

etf_url = 'http://jisilu.cn/jisiludata/etf.php'
fj_url = 'http://www.jisilu.cn/data/cf/cf_list/'
kzj_url = 'http://www.jisilu.cn/data/cbnew_ajax/get_aqd_cb_list/'

#程序
bond_raw = bond_raw(bond_url)
bond_high = bond_high(bond_raw, user_profit)
bond_max = bond_max(bond_high)
etf_high = etf(etf_url)
fj = fj(fj_url)
kzj = kzj(kzj_url)

#打印index
print_html(bond_high, bond_max, etf_high, fj, kzj)

#打印指数
print_indice_head()
print_indice('SHI:SHH')
print_indice('INX:IOM')
print_indice('HSI:HKG')
print_indice('FTPP:FSI')
print_indice('FTSE:FSI')

html_end()

#邮件
title = '今日PMONEY金融 (为了%s定制),(债券最高收益:%s)' % (user_name, bond_max)

if len(bond_high) !=0:
    print 'Meet bond value to send email'
    email(True, title, user_email)
