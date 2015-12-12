#! /usr/bin/python

from readuser import read_user
import bond

user = read_user(0)

user_seq = user['1'][0]
user_name = user['1'][1]
user_profit = user['1'][2]
user_email = user['1'][3]

print "current setup is for %s, number is %s, profit target %s, email is %s" % (user_name, user_seq, user_profit, user_email)
#print type(user_email)

bond_raw = bond.find_value()

result = bond.high_bond(bond_raw, user_profit)

bond.send(result, user_name, user_email)
