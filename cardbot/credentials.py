path = ('/Users/developer/Desktop/credentials.txt')

credentials_file = open(path, "r")

#bot token
token = credentials_file.readline()[0:-1]

#Database Credentials
user = credentials_file.readline()[0:-1]
password = credentials_file.readline()[0:-1]
host = credentials_file.readline()[0:-1]
port = credentials_file.readline()[0:-1]
database = credentials_file.readline()
db_credentials = [user, password, host, port, database]
