#! /usr/bin/python
#-*- encoding: utf-8 -*-

import os

def user(user_file, id):
	f = open(user_file)
	users_lines = f.readlines()
	f.close()
	users_profile ={}

	for user_line in users_lines:
		name = user_line.split(':')[0]
		target = user_line.split(':')[1]
		email = user_line.split(':')[2].rstrip('\n')
		users_profile[name] = (name, target, email)
	
	for user in users_profile:
	    if user == id:
	        return users_profile[user]

def email(confirm, title, user_email, url_index):
	if confirm is True:
		command = "mail -s '%s' %s < %s" % (title, user_email, url_index)
		#print command
		os.system(command)
		print "Email sent!"
	else:
		print "None find!"

    
if __name__ == "__main__":
    user_file = 'user.txt'
    id = 'hechaosb'
    user_profile = user(user_file, id)
    print user_profile


