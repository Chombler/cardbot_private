import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from cardobject import cardObject
from heroobject import heroObject

#Participant Functions
def registerParticipant(discordName, timezoneid):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_insert_query = '''
		INSERT INTO participant(discord_username, timezone_id)
		VALUES (%s,%s)
		'''

		cursor.execute(postgres_insert_query, (discordName, timezoneid))
		connection.commit()
		print("Participant logged in \"participant\"")

		postgres_select_query = '''
		SELECT discord_username, timezone_id
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

		cursor.execute(postgres_select_query, (registration_info[1],))

		timezone_info = cursor.fetchall()[0]

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return("%s, you registered in the timezone %s, which has a UTC offset of %s" % (registration_info[0], timezone_info[0], timezone_info[1]))

def isRegistered(discordName):
	is_registered_and_id = []
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_select_query = '''
		SELECT id FROM participant
		WHERE discord_username = %s
		'''

		cursor.execute(postgres_select_query, (discordName,))

		results = cursor.fetchall()

		if(len(results) > 0):
			is_registered_and_id = [True, results[0][0]]
			print("Participant is already registered in \"participant\"")
		else:
			print("Participant is not registered in \"participant\"")

	except (Exception, psycopg2.Error) as error :
		is_registered_and_id = [False, results[0][0]]
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(is_registered_and_id)

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

		print("Timezone id: %s" % (results))
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

def createTournament(tournament_name, number_of_bans, require_ign, creator_name):
	success = True
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_insert_query = '''
		INSERT INTO tournament(name, number_of_bans, require_ign, creator)
		VALUES (%s,%s,%s,%s)
		'''

		cursor.execute(postgres_insert_query, (tournament_name, number_of_bans, require_ign, creator_name))
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

def verifyTournament(tournament_name):
	success = True
	id_and_bans = []
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_table_query = '''
		SELECT id, number_of_bans, require_ign
		FROM tournament
		WHERE SIMILARITY(LOWER(name), LOWER(%s)) > 0.5
		LIMIT 1'''

		cursor.execute(select_table_query, (tournament_name,))
		results = cursor.fetchall()

		print(results)

		if(len(results) > 0):
			id_and_bans = [results[0][0], results[0][1], results[0][2]]
			print("A tournament with id %s exists" % (id_and_bans[0]))
		else:
			success = False

	except (Exception, psycopg2.Error) as error :
		success = False
		print ("Error logging request in verifyTournament,", error)
	finally:
		#closing database connection
		id_and_bans.insert(0, success)
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(id_and_bans)

def hasJoined(participant_id, tournament_id):
	already_joined = True
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_table_query = '''
		SELECT id
		FROM participant_to_tournament
		WHERE participantid = %s
		AND tournamentid = %s
		'''

		cursor.execute(select_table_query, (participant_id, tournament_id))
		results = cursor.fetchall()

		print(results)

		if(len(results) > 0):
			print("Participant is already in the tournament")
		else:
			already_joined = False


	except (Exception, psycopg2.Error) as error :
		already_joined = False
		print ("Error logging request in verifyTournament,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def joinTournament(participant_id, tournament_id):
	returnid = 0
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_insert_query = '''
		INSERT INTO participant_to_tournament(participantid, tournamentid)
		VALUES (%s,%s)
		'''

		cursor.execute(postgres_insert_query, (participant_id, tournament_id))
		connection.commit()

		postgres_select_query = '''
		SELECT id
		FROM participant_to_tournament
		WHERE participant_id = %s
		'''

		cursor.execute(postgres_select_query, (participant_id, tournament_id))

		returnid = cursor.fetchall()[0][0]

		print("Participant added to tournament")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(returnid)

def joinBan(part_to_tournament_id, hero_id):
	returnid = 0
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_insert_query = '''
		INSERT INTO tournament_participant_to_bans(tournament_to_participant_id, hero_id)
		VALUES (%s,%s)
		'''

		cursor.execute(postgres_insert_query, (part_to_tournament_id, hero_id))
		connection.commit()

		print("Participant added to tournament")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def joinIGN(part_to_tournament_id, ign):
	returnid = 0
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		postgres_insert_query = '''
		INSERT INTO tournament_participant_to_ign(tournament_to_participant_id, ign)
		VALUES (%s,%s)
		'''

		cursor.execute(postgres_insert_query, (part_to_tournament_id, ign))
		connection.commit()

		print("Participant added to tournament")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def startTournament(tournament_name, discordName):
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

def reportResult(tournament_name, discordName):
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

