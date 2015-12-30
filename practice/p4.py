#! /usr/bin/python

st = raw_input("enter:")

def check(y):		
	for x in range(0,len(y)/2,1):
		if y[x] == y[len(y)-x-1]:
			print str(x) + "is True"
#			return True
		else:
			print "failed on checking at: " + str(x)
			return False

if check(st) == False:
	print "faile!!"
else:
	print "good!!"
