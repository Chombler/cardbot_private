import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, rarity, side, trait, tribe
#Function names:
#createTable()
#dropTable()
#addToTable(recordId, recordValues)
#deleteFromTable(recordId)
#pullFromTable(recordId)
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
#16 - Pineclone
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

#card.addToTable((1, 'Forget-Me-Nuts',	1,	2,	1,	'Zombie tricks cost 1:Brain: more.',	'\"I\'d forget my own flower if it wasn\'t stuck to my head. Wait, what were we talking about?\"',	NULL,	0,	1))
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
	print ( connection.get_dsn_parameters(),"\n")

	postgres_insert_query = """ INSERT INTO card VALUES (1, 'Forget-Me-Nuts',	1,	2,	1,	'Zombie tricks cost 1:Brain: more.',	'\"I\'\'d forget my own flower if it wasn\'\'t stuck to my head. Wait, what were we talking about?\"',	NULL,	0,	1)"""
	cursor.execute(postgres_insert_query)

	connection.commit()
	print("Row added to \"card\"")

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

"""
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

	join_table_query = '''
	SELECT	card.*,
			cardclass.cardclass,
			cardset.cardset,
			rarity.rarity,
			side.side,
			trait.trait,
			tribe.tribe
	FROM card
	JOIN cardtoclass ON card.id = cardtoclass.cardid
	JOIN cardclass ON cardtoclass.classid = cardclass.id
	LEFT JOIN cardtotrait ON card.id = cardtotrait.cardid
	LEFT JOIN trait ON cardtotrait.traitid = trait.id
	LEFT JOIN cardtotribe ON card.id = cardtotribe.cardid
	LEFT JOIN tribe ON cardtotribe.id = tribe.id
	JOIN cardset ON card.id = cardset.id
	JOIN rarity ON card.id = rarity.id
	JOIN side ON card.id = side.id
	'''

	cursor.execute(check_table_query)
	results = cursor.fetchall()

	print("Printing Table")
	for row in results:
		for col in row:
			print(col)

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
			print("PostgreSQL connection is closed")"""


