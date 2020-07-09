import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, cardtype, constructor, rarity, side, trait, tribe
from cardobject import cardObject
from constructorRows import constructor_rows

#Function names:
#createTable()
#dropTable()
#addToTable(record)
#addManyToTable(recordTuple)
#deleteFromTable(recordId)
#pullFromTable(recordId)
#pullidFromTable(recordValue)
"""
tempString = "('Bubble Up',	'Guardian',	'Superpower Trick',	1,	0,	0,	'',	'Move a Plant. It gets +4:Health:.',	'Who doesn\'\'t like bubbles? Zombies...that\'\'s who.',	'',	'Super-Rare',	'Sun'),\
('Ensign Uproot',	'Guardian',	'Root Superpower Plant',	1,	2,	2,	'',	'When played: Move another Plant or Zombie.',	'His mighty tractor beam is straight off the farm and out of this world.',	'',	'Super-Rare',	'Sun'),\
('Forget-Me-Nuts',	'Guardian',	'Flower Nut Plant',	1,	2,	1,	'',	'Zombie tricks cost 1:Brain: more.',	'\"I\'\'d forget my own flower if it wasn\'\'t stuck to my head. Wait, what were we talking about?\"',	'',	'Event',	'Sun'),\
('Galacta-Cactus',	'Guardian',	'Flower Cactus Plant',	1,	2,	2,	'Bullseye',	'When Destroyed: Do 1 damage to everything.',	'\"I take pity on no one. For I am Galacta-Cactus!\"',	'Galactic',	'Super-Rare',	'Sun'),\
('Garlic',	'Guardian',	'Root Plant',	1,	1,	5,	'Team-Up',	'Whenever a Zombie hurts this, move that Zombie to that left. If that zombie is a Vimpire, destroy it.',	'\"Vimpires. They\'\'re the worst. I don\'\'t like to use the word \"hate\" but yeah, I hate \'\'em.\"',	'',	'Event',	'Sun'),\
('Grape Responsibility',	'Guardian',	'Berry Trick',	1,	0,	0,	'',	'Double a plant\'\'s health.',	'When you think of responsibility, think of grapes.',	'Colossal',	'Uncommon',	'Sun'),\
('Nut Signal',	'Guardian',	'Nut Superpower Trick',	1,	0,	0,	'',	'Make a Wall-Nut.\nDraw a card.',	'Call on Wall-Nut any time. His schedule is wide open.',	'',	'Super-Rare',	'Sun'),\
('Photosynthesizer',	'Guardian',	'Trick',	1,	0,	0,	'',	'A plant gets +2:Health:. Conjure a Galactic Gardens card.',	'\"The galaxy is one beautiful melody, so play!',	'Galactic',	'Uncommon',	'Sun'),\
('Potato Mine',	'Guardian',	'Root Plant',	1,	0,	1,	'Team-Up',	'When Destroyed: Do 2 damage to a zombie here.',	'\"I\'\'m starchy and explosive!\"',	'Premium',	'Uncommon',	'Sun'),\
('Primal Potato Mine',	'Guardian',	'Root Plant',	1,	0,	1,	'',	'When Destroyed: Do 3 damage to a zombie here.',	'Hidden long ago in Hollow Earth, Dinosaurs ran rampant in The Land Before Mine.',	'Colossal',	'Uncommon',	'Sun')"
"""
constructor.dropTable()
constructor.createTable()
constructor.addToTable(constructor_rows)

card.dropTable()
cardtoclass.dropTable()
cardtotrait.dropTable()
cardtotribe.dropTable()

card.createTable()
cardtoclass.createTable()
cardtotrait.createTable()
cardtotribe.createTable()

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
		record_name = row[1]
		record_classes = row[2].split(", ")
		record_tribesandtype = row[3].split()
		record_cost = row[4]
		record_strength = row[5]
		record_health = row[6]
		record_traits = row[7].split(", ")
		record_ability = row[8]
		record_flavor = row[9]
		record_cardset = row[10]
		record_rarity = row[11]
		record_side = row[12]
		record_cardtype = record_tribesandtype[-1]
		record_tribes = record_tribesandtype[0:-1]

		setid = cardset.pullidFromTable(record_cardset) if record_cardset is not None else None
		rarityid = rarity.pullidFromTable(record_rarity)
		typeid = cardtype.pullidFromTable(record_cardtype)
		sideid = side.pullidFromTable(record_side)

		card_record = (record_name, record_cost, record_strength, record_health, record_ability, record_flavor, setid, rarityid, sideid, typeid)

		print("\n(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % card_record)
		card.addToTable(card_record)
		cardid = card.pullidFromTable(record_name)
		print("cardid: " + str(cardid))

		for record_class in record_classes:
			print("Record Class: %s" % record_class)
			classid = cardclass.pullidFromTable(record_class)
			record_cardtoclass = (cardid, classid)
			print("Record Tuple: %s" % str(record_cardtoclass))
			cardtoclass.addToTable(record_cardtoclass)

		for record_trait in record_traits:
			if(len(record_trait) < 1):
				continue
			print("Record Trait: %s" % record_trait)
			traitid = trait.pullidFromTable(record_trait)
			record_cardtotrait = (cardid, traitid)
			print("Record Tuple: %s" % str(record_cardtotrait))
			cardtotrait.addToTable(record_cardtotrait)

		for record_tribe in record_tribes:
			if(len(record_tribe) < 1):
				continue
			print("Record Tribe: %s" % record_tribe)
			tribeid = tribe.pullidFromTable(record_tribe)
			record_cardtotribe = (cardid, tribeid)
			print("Record Tuple: %s" % str(record_cardtotribe))
			cardtotribe.addToTable(record_cardtotribe)



	# Print PostgreSQL version
	cursor.execute("SELECT version();")
	record = cursor.fetchone()
	print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
	print ("Error working with constructor in PostgreSQL", error)
finally:
	#closing database connection.
	if(connection):
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed. Card should be built.")

