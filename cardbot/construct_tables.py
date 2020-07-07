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

