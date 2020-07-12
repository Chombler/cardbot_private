import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials

def createTable():
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		create_table_query = '''CREATE TABLE cardtodeck
								(id SERIAL PRIMARY KEY,
								cardid int,
								deckid int,
								quantity int);'''

		cursor.execute(create_table_query)
		connection.commit()
		print("Table \"cardtodeck\" Addition Successful!")

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
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		delete_table_query = '''DROP TABLE cardtodeck'''

		cursor.execute(delete_table_query)
		connection.commit()
		print("Table \"cardtodeck\" Deletion Successful!")

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
		connection = psycopg2.connect(db_credentials)
		cursor = connection.cursor()

		postgres_insert_query = """ INSERT INTO cardtodeck(cardid, deckid, quantity) VALUES"""
		cursor.execute(postgres_insert_query + record)

		connection.commit()
		print("Row added to table \"cardtodeck\"")

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
		connection = psycopg2.connect(db_credentials)
		cursor = connection.cursor()

		args_str = ','.join(cursor.mogrify("(%s,%s,%s)", x).decode("utf-8") for x in recordTuple)
		print(args_str)
		cursor.execute("INSERT INTO cardtodeck(cardid, deckid, quantity) VALUES " + args_str)

		connection.commit()
		print("Multiple rows added to \"cardtodeck\"")

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
		connection = psycopg2.connect(db_credentials)
		cursor = connection.cursor()

		postgres_delete_query = """ Delete from cardtodeck where id = %s"""
		cursor.execute(postgres_delete_query, (recordId, ))
		connection.commit()
		print("Row deleted from \"cardtodeck\"")
		
	except (Exception, psycopg2.Error) as error :
		print ("Error checking table in PostgreSQL", error)
	finally:
		#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
				print("PostgreSQL connection is closed")

def pullFromTable(recordId):
	try:
		connection = psycopg2.connect(db_credentials)
		cursor = connection.cursor()

		postgres_pull_query = """ SELECT * from cardtodeck where id = %s"""
		cursor.execute(postgres_delete_query, (recordId, ))
		results = cursor.fetchall()
		print("Results from \"cardtodeck\" where id = %s" % (recordId))
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


