import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials

def getElo(name):
	try:
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		select_query = '''
		SELECT score
		FROM elo
		WHERE name = %s'''

		cursor.execute(select_query, (name))

		elo = cursor.fetchall()[0][0]

		if(elo == None):
			createRow(name)
			elo = 1000

		print("Elo obtained")

	except (Exception, psycopg2.Error) as error :
		print ("Error logging request in request,", error)
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
		INSERT INTO elo
		VALUES (%s, 1000)
		'''

		cursor.execute(insert_query, (name))
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

def applyResults(winner, loser):
	winner_elo = getElo(winner)
	loser_elo = getElo(loser)

	print(winner_elo)
	print(loser_elo)

	winner_expected = 1 / (1 + pow(10, (loser_elo - winner_elo) / 400))
	loser_expected = 1 / (1 + pow(10, (winner_elo - loser_elo) / 400))

	winner_elo = winner_elo + 30 * (1 - winner_expected)
	loser_elo = loser_elo + 30 * (0 - loser_expected)

	print(winner_elo)
	print(loser_elo)

	updateElo(winner, winner_elo)
	updateElo(loser, loser_elo)


