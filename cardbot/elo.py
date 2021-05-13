import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials

def getElo(name, discord_id):
	try:
		elo = 0
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_query = '''
		SELECT score, name
		FROM elo
		WHERE discord_id = %s'''

		cursor.execute(select_query, (discord_id,))

		results = cursor.fetchall()
		print(results)
		print(len(results))

		if(len(results) > 0):
			elo = results[0][0]
			if(results[0][1] != name):
				updateElo()
		else:
			createRow(name, discord_id)
			elo = 1000

		print("Elo obtained")

	except (Exception, psycopg2.Error) as error :
		print ("Error retreiving score from ELO,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(elo)

def createRow(name, discord_id):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		insert_query = '''
		INSERT INTO elo(name, score, discord_id)
		VALUES (%s, 1000, %s)
		'''

		cursor.execute(insert_query, (name, discord_id))
		connection.commit()
		print("New Player added to elo")

	except (Exception, psycopg2.Error) as error :
		print ("Error creating new row in ELO,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def updateElo(name, discord_id, score):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		update_query = '''
		UPDATE elo
		SET score = %s, 
			name = %s
		WHERE discord_id = %s
		'''

		cursor.execute(update_query, (score, discord_id))
		connection.commit()
		print("Elo updated")

	except (Exception, psycopg2.Error) as error :
		print ("Error updating ELO,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def getLeaderboard():
	try:
		return_string = "__ELO__ | __Name__"
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_query = '''
		SELECT score, name
		FROM elo
		ORDER BY score DESC
		LIMIT 10'''

		cursor.execute(select_query)

		results = cursor.fetchall()
		print(results)
		name_length = 0

		for row in range(len(results)):
			return_string += "\n%-5s %s" % (results[row][0], results[row][1])

	except (Exception, psycopg2.Error) as error :
		print ("Error retreiving leaderboard from elo,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(return_string)

def calculateResults(winner, winner_id, loser, loser_id):
	start_winner_elo = getElo(winner, winner_id)
	start_loser_elo = getElo(loser, loser_id)

	winner_expected = 1 / (1 + pow(10, (start_loser_elo - start_winner_elo) / 400))
	loser_expected = 1 / (1 + pow(10, (start_winner_elo - start_loser_elo) / 400))

	final_winner_elo = round(start_winner_elo + 30 * (1 - winner_expected))
	final_loser_elo = round(start_loser_elo + 30 * (0 - loser_expected))

	return([start_winner_elo, final_winner_elo, start_loser_elo, final_loser_elo])

def applyResults(winner, winner_id, loser, loser_id):
	results = calculateResults(winner, loser)
	updateElo(winner, winner_id, results[1])
	updateElo(loser, loser_id, results[3])
	return(results)

