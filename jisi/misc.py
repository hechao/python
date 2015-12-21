#! /usr/bin/python
#-*- encoding: utf-8 -*-

import os

def read_user(user_seq):
	f = open('user.txt')
	d = f.readlines()
	f.close()
	mydict ={}

	for usr in d:
		usr_name = usr.split(':')[0]
		usr_target = usr.split(':')[1]
		usr_email = usr.split(':')[2].rstrip('\n')
		#usr_email = usr.split(':')[3]
		mydict[usr_name] = (usr_name, usr_target, usr_email)
		#print mydict

	return mydict

def email(confirm, title, user_email):
	if confirm is True:
		command = "mail -s '%s' %s < /srv/www/index.html" % (title, user_email)
		#print command
		os.system(command)
		print "Email sent!"
	else:
		print "None find!"

    
#if __name__ == "__main__":

