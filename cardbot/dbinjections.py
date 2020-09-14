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

def verifyTournament(tournament_name):
	success = True
	name_and_bans = []
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_table_query = '''
		SELECT name, number_of_bans
		FROM tournament
		WHERE SIMILARITY(LOWER(name), LOWER(%s)) > 0.5
		LIMIT 1'''

		cursor.execute(select_table_query, (tournament_name,))
		results = cursor.fetchall()

		print(results)

		if(len(results) > 0):
			name_and_bans = [results[0][0], results[0][1]]
		else:
			success = False

		print("Tournament '%s' exists" % (name_and_bans[0]))

	except (Exception, psycopg2.Error) as error :
		success = False
		print ("Error logging request in verifyTournament,", error)
	finally:
		#closing database connection
		name_and_bans.insert(0, success)
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(name_and_bans)


def registerParticipant(discordName, inGameName, timezoneid):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_insert_query = '''
		INSERT INTO participant(discord_username, in_game_username, timezone_id)
		VALUES (%s,%s,%s)
		'''

		cursor.execute(postgres_insert_query, (discordName, inGameName, timezoneid))
		connection.commit()
		print("Participant logged in \"participant\"")

		postgres_select_query = '''
		SELECT discord_username, in_game_username, timezone_id
		FROM participant
		WHERE discord_username = %s
		'''

		cursor.execute(postgres_select_query, (discordName,))

		registration_info = cursor.fetchall()[0]
		print(registration_info)

		postgres_select_query = '''
		SELECT abbreviation, utc_offset
		FROM timezone
		WHERE id = %s
		'''

		cursor.execute(postgres_select_query, (registration_info[2],))

		timezone_info = cursor.fetchall()[0]

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return("%s, you registered as %s in the timezone %s, which has a UTC offset of %s" % (registration_info[0], registration_info[1], timezone_info[0], timezone_info[1]))

def isRegistered(discordName):
	name_is_registered = False
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_select_query = '''
		SELECT discord_username FROM participant
		WHERE discord_username = %s
		'''

		cursor.execute(postgres_select_query, (discordName,))

		results = cursor.fetchall()

		if(len(results) > 0):
			name_is_registered = True

		print("Participant logged in \"participant\"")

	except (Exception, psycopg2.Error) as error :
		name_is_registered = False
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(name_is_registered)

def deRegister(discordName):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_delete_query = '''
		DELETE FROM participant
		WHERE discord_username = %s
		'''

		cursor.execute(postgres_delete_query, (discordName,))
		connection.commit()

		print("Participant removed from \"participant\"")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def getTimezoneId(timezone_abbreviation):
	return_timezone_id = 0
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_select_query = '''
		SELECT id from timezone
		ORDER BY SIMILARITY(LOWER(abbreviation), LOWER(%s)) DESC
		LIMIT 1
		'''

		cursor.execute(postgres_select_query, (timezone_abbreviation,))
		connection.commit()
		results = cursor.fetchall()

		print(results)
		return_timezone_id = results[0][0]

	except (Exception, psycopg2.Error) as error :
		return_timezone_id = 0
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(return_timezone_id)

def createTournament(tournament_name, number_of_bans, creator_name):
	success = True
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_insert_query = '''
		INSERT INTO tournament(name, number_of_bans, creator)
		VALUES (%s,%s,%s)
		'''

		cursor.execute(postgres_insert_query, (tournament_name, number_of_bans, creator_name))
		connection.commit()
		print("Tournament '%s' created" % (tournament_name))

	except (Exception, psycopg2.Error) as error :
		success = False
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(success)


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


