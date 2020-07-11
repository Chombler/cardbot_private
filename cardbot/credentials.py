

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
	database = credentials_file.readline()[0:-1]
	user = credentials_file.readline()[0:-1]
	password = credentials_file.readline()[0:-1]
	host = credentials_file.readline()[0:-1]
	port = credentials_file.readline()
	db_credentials = [user, password, host, port, database]

