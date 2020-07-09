import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, cardtype, constructor, nickname, rarity, side, trait, tribe
from cardobject import cardObject
from constructorRows import constructor_rows

#Function names:
#createTable()
#dropTable()
#addToTable(record)
#addManyToTable(recordTuple)
#deleteFromTable(recordId)
#pullFromTable(recordId)
#pullColumnFromTable(pullColumn, identifier, identifyingValue)
#1 - Animal
#2 - Banana
#3 - Bean
#4 - Berry
#5 - Cactus
#6 - Corn
#7 - Dragon
#8 - Flower
#9 - Flytrap
#10 - Fruit
#11 - Leafy
#12 - Moss
#13 - Mushroom
#14 - Nut
#15 - Pea
#16 - Pinecone
#17 - Root
#18 - Seed
#19 - Squash
#20 - Tree
#21 - Mime
#22 - Barrel
#23 - Clock
#24 - Dancing
#25 - Gargantuar
#26 - Gourmet
#27 - History
#28 - Imp
#29 - Monster
#30 - Mustache
#31 - Party
#32 - Pet
#33 - Pirate
#34 - Professional
#35 - Science
#36 - Sports

"""
constructor.dropTable()
constructor.createTable()
constructor.addToTable(constructor_rows)

"""


def pullCardRecord(recordName):
	success = True
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

		select_table_query = '''
		SELECT name
		FROM nickname
		ORDER BY SIMILARITY(nickname, %s) DESC
		LIMIT 1'''

		cursor.execute(select_table_query, (recordName,))

		results = cursor.fetchall()
		print(results)
		resultname = results[0][0]

		select_table_query = '''
		SELECT id
		FROM card
		ORDER BY SIMILARITY(name, %s) DESC
		LIMIT 1'''

		cursor.execute(select_table_query, (resultname,))

		results = cursor.fetchall()
		print(results)
		resultid = results[0][0]

		join_table_query = '''
		SELECT	name, 
				cardclass.cardclass,
				tribe.tribe, cardtype.cardtype,
				cost, side.side, strength, trait.strengthmodifier, health, trait.healthmodifier,
				trait.trait,
				ability,
				flavor,
				cardset.cardset,
				rarity.rarity
		FROM card
		LEFT JOIN cardtoclass ON card.id = cardtoclass.cardid
		LEFT JOIN cardclass ON cardtoclass.classid = cardclass.id
		LEFT JOIN cardtotrait ON cardtotrait.cardid = card.id
		LEFT JOIN trait ON cardtotrait.traitid = trait.id
		LEFT JOIN cardtotribe ON card.id = cardtotribe.cardid
		LEFT JOIN tribe ON cardtotribe.tribeid = tribe.id
		LEFT JOIN cardtype ON cardtype.id = card.typeid
		LEFT JOIN cardset ON cardset.id = card.setid
		LEFT JOIN rarity ON card.rarityid = rarity.id
		LEFT JOIN side ON card.sideid = side.id
		WHERE card.id = %s
		'''

		cursor.execute(join_table_query, (resultid,))
		results = cursor.fetchall()


		print("Printing Table")
		for row in results:
			for col in row:
				print(col)
			print()

		cardInstance = cardObject(results)
		print(cardInstance.information())

		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record,"\n")

	except (Exception, psycopg2.Error) as error :
		print ("Error retrieving card information using PostgreSQL,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
		return(cardInstance.information())


