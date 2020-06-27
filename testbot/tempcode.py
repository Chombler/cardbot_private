
recordTuple = [
('Animal',),
('Banana',),
('Bean',),
('Berry',),
('Cactus',),
('Corn',),
('Dragon',),
('Flower',),
('Flytrap',),
('Fruit',),
('Leafy',),
('Moss',),
('Mushroom',),
('Nut',),
('Pea',),
('Pinecone',),
('Root',),
('Seed',),
('Squash',),
('Tree',),
('Mime',),
('Barrel',),
('Clock',),
('Dancing',),
('Gargantuar',),
('Gourmet',),
('History',),
('Imp',),
('Monster',),
('Mustache',),
('Party',),
('Pet',),
('Pirate',),
('Professional',),
('Science',),
('Sports',)]


recordTuple = [
('Guardian',),
('Kabloom',),
('Mega',),
('Smarty',),
('Solar',),
('Beastly',),
('Brainy',),
('Crazy',),
('Hearty',),
('Sneaky',)]

recordTuple = [
('Basic',),
('Premium',),
('Galactic Gardens',),
('Colossal Fossils',),
('Triassic Triumph',)]

recordTuple = [
('Plant',),
('Zombie',),
('Trick',)]

recordTuple = [
('Common',),
('Uncommon',),
('Rare',),
('Super-Rare',),
('Legendary',),
('Event')]

recordTuple = [
('Brain',),
('Sun',)]

recordTuple = [
('Amphibious', DEFAULT, DEFAULT),
('Anti-Hero 2', 'AntiHero', DEFAULT),
('Anti-Hero 3', 'AntiHero', DEFAULT),
('Anti-Hero 4', 'AntiHero', DEFAULT),
('Anti-Hero 5', 'AntiHero', DEFAULT),
('Armored 1', DEFAULT, 'Armored'),
('Armored 2', DEFAULT, 'Armored'),
('Bullseye', 'Bullseye', DEFAULT),
('Deadly', 'Deadly', DEFAULT),
('Double Strike', 'DoubleStrike', DEFAULT),
('Frenzy', 'Frenzy', DEFAULT),
('Gravestone', DEFAULT, DEFAULT),
('HealthStrength', DEFAULT, 'healthstrength'),
('Overshoot 2', 'Overshoot', DEFAULT),
('Overshoot 3', 'Overshoot', DEFAULT),
('Strikethrough', 'Strikethrough', DEFAULT),
('Team-Up', DEFAULT, DEFAULT),
('Untrickable', DEFAULT, 'Untrickable')]

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

	print("Made it")
	args_str = ','.join(cursor.mogrify("(%s)", x).decode("utf-8") for x in recordTuple)
	print("Made it again")
	print(args_str)
	cursor.execute("INSERT INTO tribe(tribe) VALUES " + args_str)

	connection.commit()
	print("Rows added to \"tribe\"")

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




#multiAddToTable()
"""card.createTable()
cardclass.createTable()
cardset.createTable()
cardtoclass.createTable()
cardtotrait.createTable()
cardtotribe.createTable()
rarity.createTable()
side.createTable()
trait.createTable()
tribe.createTable()"""
#card.addToTable((1, 'Forget-Me-Nuts',	1,	2,	1,	'Zombie tricks cost 1:Brain: more.',	'\"I\'d forget my own flower if it wasn\'t stuck to my head. Wait, what were we talking about?\"',	NULL,	0,	1))

"""try:
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
	SELECT	name, cost, strength, health, ability, flavor,
			cardclass.class,
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
	LEFT JOIN tribe ON cardtotribe.tribeid = tribe.id
	JOIN cardset ON cardset.id = card.cardset
	JOIN rarity ON card.rarity = rarity.id
	JOIN side ON card.side = side.id
	'''

	cursor.execute(join_table_query)
	results = cursor.fetchall()

	print("Printing Table")
	for row in results:
		for col in row:
			print(col)
		print()

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


