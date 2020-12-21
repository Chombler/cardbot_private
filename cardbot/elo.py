import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials

def getElo(name):
	try:
		elo = 0
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_query = '''
		SELECT score
		FROM elo
		WHERE name = %s'''

		cursor.execute(select_query, (name,))

		results = cursor.fetchall()
		print(results)
		print(len(results))

		if(len(results) > 0):
			elo = results[0][0]
		else:
			createRow(name)
			elo = 1000

		print("Elo obtained")

	except (Exception, psycopg2.Error) as error :
		print ("Error retreiving score from elo,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(elo)

def createRow(name):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		insert_query = '''
		INSERT INTO elo(name, score)
		VALUES (%s, 1000)
		'''

		cursor.execute(insert_query, (name,))
		connection.commit()
		print("New Player added to elo")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def updateElo(name, score):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		update_query = '''
		UPDATE elo
		SET score = %s
		WHERE name = %s
		'''

		cursor.execute(update_query, (score, name))
		connection.commit()
		print("Elo updated")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

def getLeaderboard():
	try:
		return_string = ""
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_query = '''
		SELECT name, score
		FROM elo
		ORDER BY score DESC
		LIMIT 10'''

		cursor.execute(select_query)

		results = cursor.fetchall()
		print(results)
		name_length = 0
		for row in range(len(results)):
			name_length = len(results[row][0]) if name_length < len(results[row][0]) else name_length

		return_string = "__Rank__ |%*s__Name__%*s| __ELO__" % (round(name_length / 2), " ", round(name_length / 2), " ")

		for row in range(len(results)):
			return_string += "\n %-8s %-*s %s" % (row + 1, name_length, results[row][0], results[row][1])
			
	except (Exception, psycopg2.Error) as error :
		print ("Error retreiving leaderboard from elo,", error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(return_string)

def calculateResults(winner, loser):
	start_winner_elo = getElo(winner)
	start_loser_elo = getElo(loser)

	winner_expected = 1 / (1 + pow(10, (start_loser_elo - start_winner_elo) / 400))
	loser_expected = 1 / (1 + pow(10, (start_winner_elo - start_loser_elo) / 400))

	final_winner_elo = round(start_winner_elo + 30 * (1 - winner_expected))
	final_loser_elo = round(start_loser_elo + 30 * (0 - loser_expected))

	return([start_winner_elo, final_winner_elo, start_loser_elo, final_loser_elo])

def applyResults(winner, loser):
	results = calculateResults(winner, loser)
	updateElo(winner, results[1])
	updateElo(loser, results[3])
	return(results)

