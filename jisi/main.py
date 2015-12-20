#! /usr/bin/python

from misc import read_user, email, log
from bond import bond_raw, bond_high, bond_max
import datetime

user = read_user(0)

ID = 'hechao'

user_name = user[ID][0]
user_profit = user[ID][1]
user_email = user[ID][2]

print "current user name is %s, profit target %s, email is %s" % (user_name, user_profit, user_email)

#print type(user_email)

date = str(datetime.datetime.now()) + "\n" +'<br>'
log(date)
log('<br>')

bond_raw = bond_raw()
bond_high = bond_high(bond_raw, user_profit)
bond_max = bond_max(bond_high)
log('<br>')

email(bond_high, bond_max, user_name, user_email)
