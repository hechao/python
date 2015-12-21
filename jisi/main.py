#! /usr/bin/python
#-*- encoding: utf-8 -*-

from misc import read_user, email, log_a, log_w
from bond import bond_raw, bond_high, bond_max
import datetime
from etf import etf

user = read_user(0)

ID = 'hechao'

user_name = user[ID][0]
user_profit = user[ID][1]
user_email = user[ID][2]

#print "* Current user name is %s, profit target %s, email is %s" % (user_name, user_profit, user_email)

bond_url = 'http://www.jisilu.cn/data/bond/?do_search=&sort_column=&sort_order=&forall=1&from_rating_cd=A&from_issuer_rating_cd=A&from_year_left=0&from_repo=0&from_ytm=4&from_volume=0&from_market=&y1=&y2=&to_rating_cd=AAA&to_issuer_rating_cd=AAA&to_year_left=25&to_repo=2&to_ytm=30&to_volume='

etf_url = 'http://jisilu.cn/jisiludata/etf.php'

#打印头部
date = '(英文版) 生成时间'+str(datetime.datetime.now()) + "\n" +'<br>'
log_w(date)
log_a('<br>')

#债券打印到index
log_a('<br>')
log_a('###以下是债券的收益信息：### <br>')
log_a('<br>')

bond_raw = bond_raw(bond_url)
bond_high = bond_high(bond_raw, user_profit)
bond_max = bond_max(bond_high)
log_a('<br>')
log_a('<br>')

#ETF打印到index
etf_intro = "###以下是ETF基金信息: ###<br>\n"
etf_url_print = "URL of ETF 网址是: " + etf_url + "<br>\n"

log_a(etf_intro)
log_a('<br>')
log_a(etf_url_print)
log_a('<br>')

di_etf = etf(etf_url)
log_a('<br>')

#打印title
title = '今日PMONEY金融 (为了%s定制),(债券最高收益:%s)' % (user_name, bond_max)

#打印
email(True, title, user_email)
