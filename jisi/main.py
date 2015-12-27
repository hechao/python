#! /usr/bin/python
#-*- encoding: utf-8 -*-

from misc import read_user, email
import datetime
from print_html import print_bond, print_etf, print_fj, print_kzj, print_indice, print_funda, html_end, html_head, print_part_head

from bond import bond_raw, bond_high, bond_max
from etf import etf
from fengji import fj
from kzj import kzj
from world_indice import indice, indice_filter
from funda import funda_raw, funda


#用户
user = read_user(0)
ID = 'hechao'
user_name = user[ID][0]
user_profit = user[ID][1]
user_email = user[ID][2]

#print "* Current user name is %s, profit target %s, email is %s" % (user_name, user_profit, user_email)

#URL
bond_url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

etf_url = 'http://jisilu.cn/jisiludata/etf.php'
fj_url = 'http://www.jisilu.cn/data/cf/cf_list/'
kzj_url = 'http://www.jisilu.cn/data/cbnew_ajax/get_aqd_cb_list/'
indice_url = ''
funda_url = 'http://www.jisilu.cn/data/sfnew/funda_list/'

#程序

html_head()

bond_raw = bond_raw(bond_url)
bond_high = bond_high(bond_raw, user_profit)
bond_max = bond_max(bond_high)
print_bond(bond_high, bond_max)

etf = etf(etf_url)
print_etf(etf)

fj = fj(fj_url)
print_fj(fj)

kzj = kzj(kzj_url)
print_kzj(kzj)

indice_dt_update = indice()
indice_filter = indice_filter(indice_dt_update, 25)
print_indice(indice_dt_update, indice_filter)

funda_raw = funda_raw(funda_url)
funda = funda(funda_raw, 10, 5, 0)
print_funda(funda)
    
html_end()

#邮件
title = '今日PMONEY金融 (为了%s定制),(债券最高收益:%s)' % (user_name, bond_max)

if len(bond_high) !=0:
    print 'Meet bond value to send email'
    email(True, title, user_email)
