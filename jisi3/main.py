#! /usr/bin/python
#-*- encoding: utf-8 -*-

from fengji import fj
from bond import bond_raw, bond_high, bond_max
from etf import etf
from kzj import kzj
from world_indice import indice, indice_filter
from funda import funda_raw, funda

from html import replace_html, print_fj, print_bond, print_etf, print_kzj, print_indice, print_funda
from datetime import datetime
import sys
from misc import read_user, email

reload(sys)  
sys.setdefaultencoding('utf8')
    
index = '/srv/www/index.html'
f = open('template.html')
fn = open(index, 'w')
pgt = '今日PMONEY金融,订阅客户:hechao!'
m1 = '* 有些投资机会和窗口转瞬即逝, 抓住机会，轮动收益<br>* 包括的信息有 传统封基，债券，ETF，可转债，国际主要指数index，分级基金<br>* (英文版) 本站网址是:http://42.120.16.247/<br>* 添加新功能：主要指数信息，打新股reminder<br>'
m2 = datetime.now().strftime('* 网页更新时间: %y-%m-%d %I:%M:%S %p <br>\n')

#fj
fj_title = '以下是传统封基的收益信息:'
fj_url = 'http://www.jisilu.cn/data/cf/cf_list/'

fj = fj(fj_url, 12)
fj_str = print_fj(fj, fj_url, index)

#bond
bond_title = '以下是债券的收益信息:'
bond_url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

bond_raw = bond_raw(bond_url)
bond_high = bond_high(bond_raw, 9)
bond_max = bond_max(bond_high)

bond_str = print_bond(bond_high, bond_max, bond_url, index)

#ETF
etf_title = '以下是ETF基金的收益信息:'
etf_url = 'http://jisilu.cn/jisiludata/etf.php'

etf = etf(etf_url)
etf_str = print_etf(etf, etf_url, index)

#KZJ
kzj_title = '以下是可转债的收益信息:'
kzj_url = 'http://www.jisilu.cn/data/cbnew_ajax/get_aqd_cb_list/'

kzj = kzj(kzj_url, 130)
kzj_str = print_kzj(kzj, kzj_url, index)

#world_indice
indice_title = '以下是国际指数信息:'
indice_url = 'www.ft.com'

indice = indice()
indice_filter = indice_filter(indice, 25)
indice_str = print_indice(indice, indice_filter, indice_url, index)

#funda
funda_title = '以下是分级基金A的信息:'
funda_url = 'http://www.jisilu.cn/data/sfnew/funda_list/'

funda_raw = funda_raw(funda_url)
funda = funda(funda_raw, 10, 5, 0)
funda_str = print_funda(funda, funda_url, index)

replace_dict = {}
replace_dict['page_title']=pgt
replace_dict['main_title']=pgt
replace_dict['bg_line1']=m1
replace_dict['bg_line2']=m2 

replace_dict['bk_title6']=funda_title
replace_dict['bk_pg6']=funda_str

replace_dict['bk_title5']=kzj_title
replace_dict['bk_pg5']=kzj_str

replace_dict['bk_title3']=bond_title
replace_dict['bk_pg3']=bond_str

replace_dict['bk_title4']=fj_title
replace_dict['bk_pg4']=fj_str

replace_dict['bk_title2']=etf_title
replace_dict['bk_pg2']=etf_str

replace_dict['bk_title1']=indice_title
replace_dict['bk_pg1']=indice_str
    
replace_html(f, fn, replace_dict)

#用户
user = read_user(0)
ID = 'hechao'
user_name = user[ID][0]
user_profit = user[ID][1]
user_email = user[ID][2]

#邮件
title = '今日PMONEY金融 (为了%s定制),(债券最高收益:%s)' % (user_name, bond_max)

if len(bond_high) !=0:
    print 'Meet bond value to send email'
    email(True, title, user_email)


