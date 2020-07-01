import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, cardtype, constructor, rarity, side, trait, tribe
from cardobject import cardObject

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

	join_table_query = '''SELECT * FROM constructor'''

	cursor.execute(join_table_query)
	results = cursor.fetchall()


	"""print("Printing Table")
	print(results)
	for row in results:
		for col in row:
			print(col)"""

	for row in results:
		name = row[1]
		classes = row[2]
		tribesandtype = row[3].split()
		cost = row[4]
		strength = row[5]
		health = row[6]
		traits = row[7].split(",")
		ability = row[8]
		flavor = row[9]
		cardset = row[10]
		rarity = row[11]
		side = row[12]
		cardtype = tribesandtype[-1]
		tribes = tribesandtype[0:-1]


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

