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

	"""for x in mydict:
		print "This user's number is %s, user name is %s, user target profit is %s, user interval is %s)" % (x, mydict[x][1], mydict[x][2],mydict[x][3])"""

	return mydict



def email(confirm, title, user_email):
	if confirm is True:
		command = "mail -s '%s' %s < /srv/www/index.html" % (title, user_email)
		#print command
		os.system(command)
		print "Email sent!"
	else:
		print "None find!"

def log_a(data):
    log = open('/srv/www/index.html', 'a+')
    log.writelines(data)
    log.close()
    
def log_w(data):
    log = open('/srv/www/index.html', 'w')
    log.writelines(data)
    log.close()
    
#if __name__ == "__main__":

