#! /usr/bin/python

input = raw_input("input the string:   ")
lenx =len(input)

print "str length is: " + str(lenx)

print "str current is" + input[0]

for x in range(len(input)-1,-1,-1):
 print "current is  " + str(x) + "  " + input[x]

#print input[3]
