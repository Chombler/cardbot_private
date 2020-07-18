import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from cardobject import cardObject
from heroobject import heroObject

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



def logRequest(requestAuthor, requestString, requestType, fuzzyRequest):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print(connection.get_dsn_parameters(),"\n")

		if(len(requestString) < 513):
			postgres_insert_query = '''
			INSERT INTO request(author, message, typeid, is_fuzzy)
			VALUES (%s,%s,%s,%s)
			'''
			cursor.execute(postgres_insert_query, (requestAuthor, requestString, requestType, fuzzyRequest))
			connection.commit()
			print("Request logged in \"request\"")
		else:
			raise ValueError('request message was too long to store')

		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record,"\n")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")


def pullCardRecord(recordName):
	success = True
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print(connection.get_dsn_parameters(),"\n")

		select_table_query = '''
		SELECT name
		FROM nickname
		WHERE SIMILARITY(nickname, %s) > 0.25
		OR LOWER(nickname) LIKE %s
		ORDER BY SIMILARITY(nickname, %s) DESC,
		LOWER(nickname) LIKE %s DESC
		LIMIT 1'''

#		OR(1 %s)

		try:
			recordStart = recordName[0:3].lower() + '%'
		except:
			recordStart = recordName[0:].lower() + '%'

#		args_str = ','.join(cursor.mogrify("(%s)", x).decode("utf-8") for x in recordTuple)

		orString = '%'
		for word in recordName.split():
			orString += word + '%'
		orString += '%'

		cursor.execute(select_table_query, (recordName, orString, recordName, recordStart))

		results = cursor.fetchall()
		if(len(results) > 0):
			resultname = results[0][0]
			print("Result Name: " + resultname)

			select_table_query = '''
			SELECT id
			FROM card
			where name = %s'''

			cursor.execute(select_table_query, (resultname,))

			results = cursor.fetchall()
			resultid = results[0][0]
			print("Result id: " + str(resultid))

			join_table_query = '''
			SELECT	card.name,
					game_class.name,
					tribe.name,
					card_type.type,
					card.cost,
					cost_type.cost_type,
					card.strength,
					trait.strengthmodifier,
					card.health,
					trait.healthmodifier,
					trait.name,
					card.ability,
					card.flavor,
					card_set.name,
					rarity.name
			FROM card
			LEFT JOIN card_to_class ON card.id = card_to_class.cardid
			LEFT JOIN game_class ON card_to_class.classid = game_class.id
			LEFT JOIN card_to_trait ON card_to_trait.cardid = card.id
			LEFT JOIN trait ON card_to_trait.traitid = trait.id
			LEFT JOIN card_to_tribe ON card.id = card_to_tribe.cardid
			LEFT JOIN tribe ON card_to_tribe.tribeid = tribe.id
			LEFT JOIN card_type ON card_type.id = card.typeid
			LEFT JOIN card_set ON card_set.id = card.setid
			LEFT JOIN rarity ON card.rarityid = rarity.id
			LEFT JOIN cost_type ON card.cost_typeid = cost_type.id
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
		else:
			success = False

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
		return(cardInstance.information() if success else "There are no matches. Start your message with -fuzzy for close matches or -help to get a list of commands.")


def pullHeroRecord(recordName):
	success = True
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print(connection.get_dsn_parameters(),"\n")

		select_table_query = '''
		SELECT id, SIMILARITY(name, %s)
		FROM hero
		ORDER BY SIMILARITY(name, %s) DESC
		LIMIT 1'''

		cursor.execute(select_table_query, (recordName, recordName))
		nameResults = cursor.fetchall()
		print(nameResults)

		select_table_query = '''
		SELECT id, SIMILARITY(abbreviation, %s)
		FROM hero
		ORDER BY SIMILARITY(abbreviation, %s) DESC
		LIMIT 1'''

		cursor.execute(select_table_query, (recordName, recordName))
		abbreviationResults = cursor.fetchall()
		print(abbreviationResults)

		if(nameResults[0][1] > abbreviationResults[0][1]):
			resultid = nameResults[0][0]
		else:
			resultid = abbreviationResults[0][0]


		print(resultid)

		join_table_query = '''
		SELECT	hero.name,
				hero.abbreviation,
				hero_class.name AS hero_class,
				card.name,
				game_class.name,
				card.ability,
				hero.flavor
		FROM hero
		LEFT JOIN hero_to_class ON hero.id = hero_to_class.heroid
		LEFT JOIN game_class AS hero_class ON hero_to_class.classid = hero_class.id
		LEFT JOIN hero_to_card ON hero.id = hero_to_card.heroid
		LEFT JOIN card ON hero_to_card.cardid = card.id
		LEFT JOIN card_to_class ON card.id = card_to_class.cardid
		LEFT JOIN game_class ON card_to_class.classid = game_class.id
		WHERE hero.id = %s
		'''

		cursor.execute(join_table_query, (resultid,))
		results = cursor.fetchall()

		print(results)
		print("Printing Table")
		for row in results:
			for col in row:
				print(col)
			print()

		heroInstance = heroObject(results)
		print(heroInstance.information())

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
		return(heroInstance.information())


def pullFuzzyCardRecord(recordName):
	try:
		returnString = "Here are the closest matches:"
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print(connection.get_dsn_parameters(),"\n")

		select_table_query = '''
		SELECT name
		FROM nickname
		ORDER BY SIMILARITY(nickname, %s) DESC,
		LOWER(nickname) LIKE %s DESC
		LIMIT 5'''

		try:
			recordStart = recordName[0:3].lower() + '%'
		except:
			recordStart = recordName[0:].lower() + '%'

		cursor.execute(select_table_query, (recordName, recordStart))
		results = cursor.fetchall()

		for row in results:
			for col in row:
				returnString += "\n" + col

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
		return(returnString)


def pullFuzzyHeroRecord(recordName):
	try:
		returnString = "Here are the closest matches:"
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print(connection.get_dsn_parameters(),"\n")

		select_table_query = '''
		SELECT id, name, abbreviation
		FROM hero
		ORDER BY SIMILARITY(name, %s) DESC
		ORDER BY SIMILARITY(abbreviation, %s) DESC
		LIMIT 1'''

		cursor.execute(select_table_query, (recordName, recordName))
		resuts = cursor.fetchall()

		for row in results:
			returnString += "\n" = row[0] + ", (" + row[1] + ")"


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
		return(returnString)


