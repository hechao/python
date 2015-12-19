#! /usr/bin/python

from readuser import read_user
import bond

user = read_user(0)

ID = 'hechao'

user_name = user[ID][0]
user_profit = user[ID][1]
user_email = user[ID][2]

print "current user name is %s, profit target %s, email is %s" % (user_name, user_profit, user_email)

#print type(user_email)

bond_raw = bond.bond_raw()

high_bond = bond.high_bond(bond_raw, user_profit)

max_bond = bond.max_bond(high_bond)

bond.send(high_bond, max_bond, user_name, user_email)
