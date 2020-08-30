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


def logRequest(requestAuthor, requestString, requestType, fuzzyRequest):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

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

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
"""
def determineHeroSide(recordName):
	success = True
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

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

	except (Exception, psycopg2.Error) as error :
		print ("Error retrieving card information using PostgreSQL,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
		return(heroInstance.information())
"""
def registerParticipant(discordName, inGameName, timezone, plantHeroBan1, plantHeroBan2, zombieHeroBan1, zombieHeroBan2):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_insert_query = '''
		INSERT INTO participant(discord_username, in_game_username, timezone, first_plant_hero_ban, second_plant_hero_ban, first_zombie_hero_ban, second_zombie_hero_ban)
		VALUES (%s,%s,%s,%s,%s,%s,%s)
		'''

		cursor.execute(postgres_insert_query, (discordName, inGameName, timezone, plantHeroBan1, plantHeroBan2, zombieHeroBan1, zombieHeroBan2))
		connection.commit()
		print("Participant logged in \"participant\"")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")


def getBestCardMatchId(recordName):
	success = True
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_table_query = '''
		SELECT name
		FROM nickname
		WHERE SIMILARITY(nickname, %s) > 0.25
		OR LOWER(nickname) LIKE LOWER(%s)
		ORDER BY SIMILARITY(nickname, %s) DESC,
		LOWER(nickname) LIKE LOWER(%s) DESC
		LIMIT 1'''

#		OR(1 %s)

		try:
			recordStart = recordName[0:3] + '%'
		except:
			recordStart = recordName[0:] + '%'

#		args_str = ','.join(cursor.mogrify("(%s)", x).decode("utf-8") for x in recordTuple)

		orString = '%'
		for word in recordName.split():
			orString += word + '%'
		orString += '%'

		cursor.execute(select_table_query, (recordName, orString, recordName, recordStart))

		results = cursor.fetchall()
		try:
			resultname = results[0][0]
			print("Result Name: " + resultname)

			select_table_query = '''
			SELECT id
			FROM card
			where name = %s'''

			cursor.execute(select_table_query, (resultname,))

			results = cursor.fetchall()
			cardid = results[0][0]
			print("Result id: " + str(cardid))
		except:
			success = False

	except (Exception, psycopg2.Error) as error :
		print ("Error retrieving card information using PostgreSQL,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
		return(cardid if success else None)


def pullCardRecord(recordName):
	cardid = getBestCardMatchId(recordName)
	print("Result id: " + str(cardid))

	if(cardid is None):
		return("There are no matches. Start your message with -fuzzy for close matches or -help to get a list of commands.")
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

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

		cursor.execute(join_table_query, (cardid,))
		results = cursor.fetchall()

		print("Printing Table")
		for row in results:
			for col in row:
				print(col)
			print()

		cardInstance = cardObject(results)
		print(cardInstance.information())

	except (Exception, psycopg2.Error) as error :
		print ("Error retrieving card information using PostgreSQL,", error)
	finally:
		#closing database connection=
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
		return(cardInstance.information())

def getBestHeroMatchId(recordName):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

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
			heroid = nameResults[0][0]
		else:
			heroid = abbreviationResults[0][0]

	except (Exception, psycopg2.Error) as error :
		print ("Error retrieving hero information using PostgreSQL,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
		return(heroid)


def pullHeroRecord(recordName):
	heroid = getBestHeroMatchId(recordName)
	print("Hero id: " + str(heroid))

	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

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

		cursor.execute(join_table_query, (heroid,))
		results = cursor.fetchall()

		print(results)
		print("Printing Table")
		for row in results:
			for col in row:
				print(col)
			print()

		heroInstance = heroObject(results)
		print(heroInstance.information())

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

		select_table_query = '''
		SELECT name, abbreviation
		FROM hero
		ORDER BY SIMILARITY(name, %s) DESC,
		SIMILARITY(abbreviation, %s) DESC
		LIMIT 5'''

		cursor.execute(select_table_query, (recordName, recordName))
		results = cursor.fetchall()

		for row in results:
			returnString += "\n" + row[0] + " (" + row[1] + ")"


	except (Exception, psycopg2.Error) as error :
		print ("Error retrieving card information using PostgreSQL,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
		return(returnString)


