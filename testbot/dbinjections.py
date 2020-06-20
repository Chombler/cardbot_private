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
								(ID int,
								Name varchar(99),
								Cost int,
								Strength int,
								Health int,
								Ability varchar(255),
								Flavor varchar(255),
								cardset int,
								rarity int,
								side int);'''
		
		cursor.execute(create_table_query)
		connection.commit()
		print("card Table Addition Successful!")


		"""create_table_query = '''CREATE TABLE cardClass
								(ID int,
								class varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardClass Table Addition Successful!")

		create_table_query = '''CREATE TABLE Trait
								(ID int,
								class varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("Trait Table Addition Successful!")

		create_table_query = '''CREATE TABLE Tribe
								(ID int,
								tribe varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("Tribe Table Addition Successful!")

		create_table_query = '''CREATE TABLE cardSet
								(ID int,
								cardSet varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardSet Table Addition Successful!")


		create_table_query = '''CREATE TABLE Rarity
								(ID int,
								rarity varchar(16));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardRarity Table Addition Successful!")

		create_table_query = '''CREATE TABLE cardtoclass
								(ID int,
								cardId int,
								classId int);'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardtoclass Table Addition Successful!")


		create_table_query = '''CREATE TABLE cardtotribe
								(ID int,
								cardId int,
								tribeId int);'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardtotribe Table Addition Successful!")


		create_table_query = '''CREATE TABLE cardtotrait
								(ID int,
								cardId int,
								traitId int);'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardtotrait Table Addition Successful!")

		create_table_query = '''CREATE TABLE side
								(ID int,
								side varchar(10));'''

		cursor.execute(create_table_query)
		connection.commit()
		print("cardtotrait Table Addition Successful!")"""

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

		delete_table_query = '''DROP TABLE cardRarity'''

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


#Adding to database
def addToTable(recordId, value):
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
		#record_to_insert = (recordId, value)
		cursor.execute(postgres_insert_query, (1,	'Forget-Me-Nuts',	1,	2,	1,	'Zombie tricks cost 1:Brain: more.',	'\"I\'d forget my own flower if it wasn\'t stuck to my head. Wait, what were we talking about?\"',	5,	0,	1))
		#postgres_insert_query = """ INSERT INTO cardset (id, cardset) VALUES (%s,%s) """
		#cursor.execute(postgres_insert_query, (recordId, value))

		connection.commit()
		print("Row added")

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

def deleteFromTable(tableName, recordId):
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

		postgres_delete_query = """ Delete from cardset where id = %s"""
		record_to_delete = (recordId)
		cursor.execute(postgres_delete_query, (recordId, ))
		connection.commit()

		check_table_query = '''SELECT * FROM card'''

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

"""addToTable(0, 'Event')
addToTable(1, 'Common')
addToTable(2, 'Uncommon')
addToTable(3, 'Rare')
addToTable(4, 'Super-Rare')
addToTable(5, 'Legendary')"""

"""addToTable(0, 'Basic')
addToTable(1, 'Premium')
addToTable(2, 'Galactic Gardens')
addToTable(3, 'Colossal Fossils')
addToTable(4, 'Triassic Triumph')
addToTable(5, '')"""

"""deleteFromTable("", 0)
deleteFromTable("", 1)
deleteFromTable("", 2)
deleteFromTable("", 3)
deleteFromTable("", 4)
deleteFromTable("", 5)"""

"""addToTable(1, 'Guardian')
addToTable(2, 'Kabloom')
addToTable(3, 'Mega-Grow')
addToTable(4, 'Smarty')
addToTable(5, 'Solar')
addToTable(6, 'Beastly')
addToTable(7, 'Brainy')
addToTable(8, 'Crazy')
addToTable(9, 'Hearty')
addToTable(10, 'Sneaky')"""

"""addToTable(1, 'Animal')
addToTable(2, 'Banana')
addToTable(3, 'Bean')
addToTable(4, 'Berry')
addToTable(5, 'Cactus')
addToTable(6, 'Corn')
addToTable(7, 'Dragon')
addToTable(8, 'Flower')
addToTable(9, 'Flytrap')
addToTable(10, 'Fruit')
addToTable(11, 'Leafy')
addToTable(12, 'Moss')
addToTable(13, 'Mushroom')
addToTable(14, 'Nut')
addToTable(15, 'Pea')
addToTable(16, 'Pinecone')
addToTable(17, 'Root')
addToTable(18, 'Seed')
addToTable(19, 'Squash')
addToTable(20, 'Tree')
addToTable(21, 'Mime')
addToTable(22, 'Barrel')
addToTable(23, 'Clock')
addToTable(24, 'Dancing')
addToTable(25, 'Gargantuar')
addToTable(26, 'Gourmet')
addToTable(27, 'History')
addToTable(28, 'Imp')
addToTable(29, 'Monster')
addToTable(30, 'Mustache')
addToTable(31, 'Party')
addToTable(32, 'Pet')
addToTable(33, 'Pirate')
addToTable(34, 'Professional')
addToTable(35, 'Science')
addToTable(36, 'Sports')"""

"""addToTable(1, 'Plant')
addToTable(2, 'Zombie')"""

addToTable('',1)


