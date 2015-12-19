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
