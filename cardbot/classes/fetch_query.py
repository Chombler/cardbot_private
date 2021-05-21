from query.py import query
import psycopg2
from psycopg2 import Error

class fetch_query(query):
	def __init__(self, query_string, query_confirmation, query_error):
		super(query_string, query_confirmation, query_error)

	def run(*args):
		print("Trying")
		connection = psycopg2.connect(db_credentials)
		print("connected")
		cursor = connection.cursor()

		cursor.execute(self.query, args)

		results = cursor.fetchall()
		print(query_confirmation)

	except (Exception, psycopg2.Error) as error :
		print (query_error, error)
	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			return(results)


def test():
	elo_query = fetch_query('''
			SELECT score, name
			FROM elo
			WHERE discord_id = %s''', "Elo score obtained", "Error retrieving score from elo,")

	print(elo_query.run(445781406111760415))
