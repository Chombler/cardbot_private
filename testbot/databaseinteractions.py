
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

		create_table_query = '''CREATE TABLE uniqueCardAttributes
								(cardID int,
								Name varchar(99),
								Cost int,
								Strength int,
								Health int,
								Ability varchar(255),
								cardSet varchar(16),
								Rarity varchar(16),
								Flavor varchar(255));'''
		
		cursor.execute(create_table_query)
		connection.commit()
		print("uniqueCardAttributes Table Addition Successful!")


		create_table_query = '''CREATE TABLE cardToClass
								(cardID int,
								class varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardToClass Table Addition Successful!")

		create_table_query = '''CREATE TABLE cardToTraits
								(cardID int,
								class varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardToTraits Table Addition Successful!")

		create_table_query = '''CREATE TABLE cardToTribes
								(cardID int,
								tribe varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardToTribes Table Addition Successful!")

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
		print ( connection.get_dsn_parameters(),"\n")

		delete_table_query = '''DROP TABLE uniqueCardAttributes'''

		cursor.execute(delete_table_query)
		connection.commit()
		print("Table Deletion Successful!")

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

def checkTable():
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

		check_table_query = '''SELECT * FROM uniqueCardAttributes'''

		cursor.execute(check_table_query)
		results = cursor.fetchall()

		print("Printing Table")
		for row in results:
			for col in row:
				print(col)

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


