#! /usr/bin/python

import readuser
import bond

user = readuser.read_user(0)

ID = 'hechao'

user_name = user[ID][0]
user_profit = user[ID][1]
user_email = user[ID][2]

print "current user name is %s, profit target %s, email is %s" % (user_name, user_profit, user_email)

#print type(user_email)

bond_raw = bond.bond_raw()

bond_high = bond.bond_high(bond_raw, user_profit)

bond_max = bond.bond_max(bond_high)

readuser.email(bond_high, bond_max, user_name, user_email)
