#! /usr/bin/python

#
#

string = raw_input("enter: ")
string = string.lower()

def count(y):
	total = 0
	for x in y:
		if x == "a":
			total = total +1
		elif x == "e":
			total = total +1
		elif x == "i":
			total = total +1
		elif x == "o":
			total = total +1
		elif x == "u":
			total = total +1
	return total
	
print count(string)
