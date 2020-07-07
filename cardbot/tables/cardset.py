import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials

def createTable():
	try:
		print("Trying")
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		print("connected")
		cursor = connection.cursor()

		create_table_query = '''CREATE TABLE cardset
								(id SERIAL PRIMARY KEY,
								cardset varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("Table \"cardset\" Addition Successful!")

		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record,"\n")

	except (Exception, psycopg2.Error) as error :
		print ("Error adding table to PostgreSQL", error)
	finally:
		#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
				print("PostgreSQL connection is closed")

def dropTable():
	try:
		print("Trying")
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		print("connected")
		cursor = connection.cursor()

		delete_table_query = '''DROP TABLE cardset'''

		cursor.execute(delete_table_query)
		connection.commit()
		print("Table \"cardset\" Deletion Successful!")

		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record,"\n")

	except (Exception, psycopg2.Error) as error :
		print ("Error removing table from PostgreSQL", error)
	finally:
		#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
				print("PostgreSQL connection is closed")


#Adding to database
def addToTable(record):
	try:
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		cursor = connection.cursor()

		postgres_insert_query = """ INSERT INTO cardset(cardset) VALUES (%s)"""
		cursor.execute(postgres_insert_query, (record))

		connection.commit()
		print("Row added to table \"cardset\"")


	except (Exception, psycopg2.Error) as error :
		print ("Error checking table in PostgreSQL", error)
	finally:
		#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
				print("PostgreSQL connection is closed")

def addManyToTable(recordTuple):
	try:
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		cursor = connection.cursor()

		args_str = ','.join(cursor.mogrify("(%s)", x).decode("utf-8") for x in recordTuple)
		print(args_str)
		cursor.execute("INSERT INTO cardset(cardset) VALUES " + args_str)

		connection.commit()
		print("Multiple rows added to \"cardset\"")

	except (Exception, psycopg2.Error) as error :
		print ("Error checking table in PostgreSQL", error)
	finally:
		#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
				print("PostgreSQL connection is closed")

def deleteFromTable(recordId):
	try:
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		cursor = connection.cursor()

		postgres_delete_query = """ Delete from cardset where id = %s"""
		cursor.execute(postgres_delete_query, (recordId, ))
		connection.commit()
		print("Row deleted from \"cardset\"")
		
	except (Exception, psycopg2.Error) as error :
		print ("Error checking table in PostgreSQL", error)
	finally:
		#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
				print("PostgreSQL connection is closed")

def pullFromTable(column, identifier):
	try:
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		cursor = connection.cursor()

		postgres_pull_query = """ SELECT * from cardset where id = %s"""
		cursor.execute(postgres_delete_query, (recordId, ))
		results = cursor.fetchall()
		print("Results from \"cardset\" where id = %s" % (recordId))
		for row in results:
			for col in row:
				print(col, end='')
			print('')

	except (Exception, psycopg2.Error) as error :
		print ("Error checking table in PostgreSQL", error)
	finally:
		#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
				print("PostgreSQL connection is closed")

def pullidFromTable(recordValue):
	try:
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		cursor = connection.cursor()

		results = []
		postgres_pull_query = """ SELECT id from cardset where cardset = %s"""
		cursor.execute(postgres_pull_query, (recordValue,))
		results = cursor.fetchall()
		result = None
		try:
			result = results[0][0]
		except:
			result = None

	except (Exception, psycopg2.Error) as error :
		print ("Error checking table in PostgreSQL", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			#print("PostgreSQL connection is closed")
		return(result)
