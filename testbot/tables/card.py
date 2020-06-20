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
		# Print PostgreSQL Connection properties
		print ( connection.get_dsn_parameters(),"\n")

		create_table_query = '''CREATE TABLE card
								(id int,
								name varchar(99),
								cost int,
								strength int,
								health int,
								ability varchar(255),
								flavor varchar(255),
								cardset int,
								rarity int,
								side int);'''
		
		cursor.execute(create_table_query)
		connection.commit()
		print("Table \"card\" Addition Successful!")

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
		# Print PostgreSQL Connection properties
		print(connection.get_dsn_parameters(),"\n")

		delete_table_query = '''DROP TABLE card'''

		cursor.execute(delete_table_query)
		connection.commit()
		print("Table \"card\" Deletion Successful!")

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
def addToTable(recordId, recordValues):
	try:
		print("Trying")
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		print("connected")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print ( connection.get_dsn_parameters(),"\n")

		postgres_insert_query = """ INSERT INTO card (id, name, cost, strength, health, ability, flavor, cardset, rarity, side) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		cursor.execute(postgres_insert_query, (recordId, recordValues))

		connection.commit()
		print("Row added to \"card\"")

		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record,"\n")

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
		print("Trying")
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		print("connected")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print ( connection.get_dsn_parameters(),"\n")

		postgres_delete_query = """ Delete from card where id = %s"""
		cursor.execute(postgres_delete_query, (recordId, ))
		connection.commit()
		print("Row deleted from \"card\"")

		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record,"\n")

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
		print("Trying")
		connection = psycopg2.connect(user = db_credentials[0],
										password = db_credentials[1],
										host = db_credentials[2],
										port = db_credentials[3],
										database = db_credentials[4])
		print("connected")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print ( connection.get_dsn_parameters(),"\n")

		postgres_pull_query = """ SELECT * from card where id = %s"""
		cursor.execute(postgres_delete_query, (recordId, ))
		results = cursor.fetchall()
		print("Results from \"card\" where id = %s" % (recordId))
		for row in results:
			for col in row:
				print(col, end='')
			print('')

		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record,"\n")

	except (Exception, psycopg2.Error) as error :
		print ("Error checking table in PostgreSQL", error)
	finally:
		#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
				print("PostgreSQL connection is closed")
