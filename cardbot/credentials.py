

try:
	import os
	#bot token
	token = os.environ['DISCORD_TOKEN']
	db_credentials = os.environ['DATABASE_URL']
except:
	path = ('/Users/developer/Desktop/credentials.txt')

	credentials_file = open(path, "r")

	#bot token
	token = credentials_file.readline()[0:-1]

	#Database Credentials
	db_credentials = credentials_file.readline()

