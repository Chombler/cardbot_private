import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, cardtype, constructor, rarity, side, trait, tribe
from cardobject import cardObject
#Function names:
#createTable()
#dropTable()
#addToTable(record)
#addManyToTable(recordTuple)
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

rows = "('Forget-Me-Nuts',	'Guardian',	'Flower Nut Plant',	1,	2,	1,	'',	'Zombie tricks cost 1:Brain: more.',	'\"I\'\'d forget my own flower if it wasn\'\'t stuck to my head. Wait, what were we talking about?\"',	'',	'Event',	'Plant'),\
('Galacta-Cactus',	'Guardian',	'Flower Cactus Plant',	1,	2,	2,	'Bullseye',	'When Destroyed: Do 1 damage to everything.',	'\"I take pity on no one. For I am Galacta-Cactus!\"',	'Galactic',	'Super-Rare',	'Plant'),\
('Garlic',	'Guardian',	'Root Plant',	1,	1,	5,	'Team-Up',	'Whenever a Zombie hurts this, move that Zombie to that left. If that zombie is a Vimpire, destroy it.',	'\"Vimpires. They\'\'re the worst. I don\'\'t like to use the word \"hate\" but yeah, I hate \'\'em.\"',	'',	'Event',	'Plant'),\
('Grape Responsibility',	'Guardian',	'Berry Trick',	1,	0,	0,	'',	'Double a plant\'\'s health.',	'When you think of responsibility, think of grapes.',	'Colossal',	'Uncommon',	'Plant'),\
('Photosynthesizer',	'Guardian',	'Trick',	1,	0,	0,	'',	'A plant gets +2:Health:. Conjure a Galactic Gardens card.',	'\"The galaxy is one beautiful melody, so play!',	'Galactic',	'Uncommon',	'Plant'),\
('Potato Mine',	'Guardian',	'Root Plant',	1,	0,	1,	'Team-Up',	'When Destroyed: Do 2 damage to a zombie here.',	'\"I\'\'m starchy and explosive!\"',	'Premium',	'Uncommon',	'Plant'),\
('Primal Potato Mine',	'Guardian',	'Root Plant',	1,	0,	1,	'',	'When Destroyed: Do 3 damage to a zombie here.',	'Hidden long ago in Hollow Earth, Dinosaurs ran rampant in The Land Before Mine.',	'Colossal',	'Uncommon',	'Plant'),\
('Small-Nut',	'Guardian',	'Nut Plant',	1,	1,	1,	'',	'',	'A violin virtuoso, Small-Nut began taking lessons when he was still in the shell.',	'Basic',	'Common',	'Plant'),\
('Sting Bean',	'Guardian',	'Bean Pea Plant',	1,	1,	2,	'Bullseye, Amphibious',	'',	'\"I try to warn them, \'\'This is going to sting.\'\' But the Zombies, they never listen.\"',	'Basic',	'Common',	'Plant'),\
('Wall-Nut',	'Guardian',	'Nut Plant',	1,	0,	6,	'',	'Team Up',	'Works well with others. Says so, right there on his resume.',	'Basic',	'Common',	'Plant'),\
('Cactus',	'Guardian',	'Cactus Plant',	2,	1,	5,	'Bullseye',	'',	'\"It\'\'s true. I\'\'m prickly on the outside but spongy on the inside.\"',	'Premium',	'Uncommon',	'Plant'),\
('Corn Dog',	'Guardian',	'Corn Animal Plant',	2,	3,	2,	'Amphibious, Hunt',	'',	'\"Who\'\'s a good vegetable? You are! Yes, you are!\"',	'',	'Event',	'Plant'),\
('Gardening Gloves',	'Guardian',	'Trick',	2,	0,	0,	'',	'Move a plant.\nDraw a card.',	'Made of the softest fabric for that gentle Plant touch.',	'Premium',	'Uncommon',	'Plant'),\
('Grave Buster',	'Guardian',	'Root Trick',	2,	0,	0,	'',	'Destroy a Gravestone.',	'\"MUST. DESTROY. GRAVES.\"',	'Premium',	'Rare',	'Plant'),\
('Hot Date',	'Guardian',	'Fruit Plant',	2,	0,	1,	'',	'When played: Move a Zombie to this lane.\nWhen destroyed: Do 3 damage to a Zombie here.',	'He\'\'s a hot commodity on dating sites such as eGardening, Thatch.com, and OKTulip.',	'',	'Event',	'Plant'),\
('Jugger-Nut',	'Guardian',	'Nut Plant',	2,	2,	2,	'Armored 1, Bullseye',	'',	'What\'\'s better than a Wall-Nut? A Wall-Nut in a suit of armor, that\'\'s what.',	'Premium',	'Super-Rare',	'Plant'),\
('Pismashio',	'Guardian',	'Nut Plant',	2,	2,	3,	'',	'',	'\"I\'\'m a kind of ice cream! Sort of!\"',	'Basic',	'Common',	'Plant'),\
('Sea-Shroom',	'Guardian',	'Mushroom Plant',	2,	2,	2,	'Amphibious',	'',	'Teaches swimming lessons to disadvantaged Plants in his spare time.',	'Premium',	'Uncommon',	'Plant'),\
('Spikeweed Sector',	'Guardian',	'Root Environment',	2,	0,	0,	'',	'Before combat here: Do 2 damage to a Zombie here.',	'Quite similar to the region known as Pokey Province.',	'Galactic',	'Uncommon',	'Plant'),\
('Tricarrotops',	'Guardian',	'Root Animal Plant',	2,	1,	3,	'Bullseye',	'Dino Roar: This gets +1/+1,',	'Beta-Carrotina tracked Huge-Gigantacus all the way down the Meteor-Z-carved tunnel to Hollow Earth. Carrots there had evolved in a very different direction.',	'Colossal',	'Legendary',	'Plant'),\
('Water Chestnut',	'Guardian',	'Root Nut Plant',	2,	0,	8,	'Amphibious, Team-Up',	'',	'\"300 laps a day, every day. That\'\'s how I do it.\"',	'Premium',	'Uncommon',	'Plant'),\
('Health-Nut',	'Guardian',	'Nut Plant',	3,	0,	4,	'',	'This attacks with its :Health: instead of its :Strength:.',	'He always skips leg day.',	'',	'Event',	'Plant'),\
('Hibernating Beary',	'Guardian',	'Berry Animal Plant',	3,	0,	8,	'',	'When hurt: This gets +4:Strength:.',	'Don\'\'t poke the beary.',	'Premium',	'Rare',	'Plant'),\
('Marine Bean',	'Guardian',	'Bean Animal Plant',	3,	3,	2,	'Amphibious',	'When played: This gets +1/+1 for each other Amphibious Plant.',	'Of course beans evolved gills. How else would they breathe underwater?',	'Triassic',	'Super-Rare',	'Plant'),\
('Pea-Nut',	'Guardian',	'Pea Nut Plant',	3,	2,	4,	'Team-Up',	'',	'\"Mom was a Peashooter. Dad was a nut. Everyone said it wouldn\'\'t work, but they were wrong.\"',	'Premium',	'Uncommon',	'Plant'),\
('Pear Cub',	'Guardian',	'Fruit Animal Plant',	3,	1,	1,	'Amphibious',	'When destroyed: Make a 5/4 Grizzly Pea with Amphibious here.',	'So cute and cuddly and ... wait, what\'\'s that growling sound?',	'',	'Event',	'Plant'),\
('Plantern',	'Guardian',	'Tree Root Plant',	3,	3,	3,	'',	'While in an Environment: This gets +1/+1 and Bulllseye.',	'Past job experience includes: Shooing away creepy fog.',	'Galactic',	'Uncommon',	'Plant'),\
('Primal Wall-Nut',	'Guardian',	'Nut Plant',	3,	0,	9,	'Team-Up, Untrickable',	'When played: Conjure a card that costs 4:Sun: or more.',	'You can\'\'t be destroyed by a Rolling Stone when you basically are a Rolling Stone.',	'Triassic',	'Super-Rare',	'Plant'),\
('Pumpkin Shell',	'Guardian',	'Squash Plant',	3,	2,	4,	'',	'Fusion: A plant played on this gets +2/+4.',	'\"Build your house on a solid foundation,\" they said. \"Build your house on pumpkin.\"',	'Triassic',	'Rare',	'Plant'),\
('Shamrocket',	'Guardian',	'Leafy Pineclone Trick',	3,	0,	0,	'',	'Destroy a Zombie that has 4:Strength: or more.',	'The bigger they are, the harder they go boom.',	'',	'Event',	'Plant'),\
('Spineapple',	'Guardian',	'Fruit Plant',	3,	0,	3,	'',	'When Played: All plants with 0:Strength: get +2:Strength:.',	'Don\'\'t let his gruff exterior fool you. He\'\'s always looking out for the little guy.',	'Basic',	'Common',	'Plant'),\
('Steel Magnolia',	'Guardian',	'Flower Plant',	3,	2,	2,	'',	'When Played: Plants here and next door get +2:Health:.',	'She\'\'s got nerves of steel... and everything else of steel!',	'Premium',	'Uncommon',	'Plant'),\
('Three-Nut',	'Guardian',	'Pea Nut Plant',	3,	3,	2,	'',	'Whenever a plant is played, that plant\'\'s :Strength: becomes 3.',	'They say two heads are better than one. Three-Nut just took the next evolutionary step.',	'Colossal',	'Super-Rare',	'Plant'),\
('Blockbuster',	'Guardian',	'Root Plant',	4,	3,	3,	'Bulllseye',	'Plant Evolution: Destroy all Gravestones here and next door.',	'They call it a graveyard. She calls it a buffet.',	'Colossal',	'Rare',	'Plant'),\
('Cosmic Nut',	'Guardian',	'Nut Plant',	4,	3,	3,	'',	'When played: Conjure a Nut, and its :Strength: becomes 3.',	'A staunch believer in numerology, he\'\'ll go on at length about the significance of the number 3 if you let him.',	'Galactic',	'Rare',	'Plant'),\
('Force Field',	'Guardian',	'Environment',	4,	0,	0,	'',	'Plants here can\'\'t be hurt.',	'It\'\'s a force of nature.',	'Galactic',	'Super-Rare',	'Plant'),\
('Guacodile',	'Guardian',	'Fruit Animal Plant',	4,	4,	3,	'Amphibious',	'When destroyed: Do 4 damage to a Zombie here.',	'\"Technically I\'\'m a food, not a Plant.\"',	'Premium',	'Super-Rare',	'Plant'),\
('Mirror-Nut',	'Guardian',	'Nut Plant',	4,	0,	8,	'Team-Up',	'When your Nuts get hurt, do 2 damage to the Zombie Hero.',	'Dressed up as a mirrorball for a disco-themed party. Never looked back.',	'Premium',	'Super-Rare',	'Plant'),\
('Prickly Pear',	'Guardian',	'Cactus Fruit Plant',	4,	0,	4,	'Team-Up',	'When hurt: Do 4 damage to a Zombie here.',	'\"You hurt me, I hurt you. That\'\'s how this works.\"',	'Premium',	'Rare',	'Plant'),\
('Red Stinger',	'Guardian',	'Flower Plant',	4,	2,	7,	'Team-Up',	'When played behind a plant: This becomes a 7/2',	'\"I do stretching exercises every morning,\" he says. \"It\'\'s important to stay physically and mentally nimble.\"',	'',	'Event',	'Plant'),\
('Starch-Lord',	'Guardian',	'Root Plant',	4,	2,	4,	'',	'When you play a Root, that Root gets +1/+1.\nStart of turn: Conjure a Root.',	'His destiny is written in the starch.',	'Galactic',	'Rare',	'Plant'),\
('Body-Gourd',	'Guardian',	'Squash Plant',	5,	3,	6,	'Amphibious, Team-Up',	'When played: Fill your Super-Block meter to full.',	'He moonlights as a decorative center piece during the fall.',	'Galactic',	'Legendary',	'Plant'),\
('Doom-Shroom',	'Guardian',	'Mushroom Plant',	5,	0,	0,	'',	'Destroy all Plants and Zombies with 4:Strength: or more.',	'\"I could destroy everything you hold dear. It wouldn\'\'t be hard.\"',	'Premium',	'Super-Rare',	'Plant'),\
('Grizzly Pear',	'Guardian',	'Fruit Animal Plant',	5,	5,	4,	'Amphibious',	'',	'It\'\'s true what they say, \"Never get between a Grizzly Pear and her cub.\" Doubly true for Zombies.',	'Triassic',	'Uncommon',	'Plant'),\
('Peconalith',	'Guardian',	'Nut Plant',	5,	0,	7,	'',	'All Plants and Zombies attack with their :Health: instead of their :Strength:.',	'No one knows where he came from. He just appeared one day. But everyone who comes in contact with him feels... changed somehow.',	'Galactic',	'Legendary',	'Plant'),\
('Smackadamia',	'Guardian',	'Nut Plant',	5,	4,	4,	'Amphibious',	'When played: Your nuts get +2:Health:.',	'Smackadamia wasn\'\'t born with smack smarts. He studied hard. He\'\'s a smackademic.',	'Premium',	'Rare',	'Plant'),\
('Tough Beets',	'Guardian',	'Root Plant',	5,	6,	1,	'Armored 1',	'When played: This gets +1:Health: for every other Plant and Zombie.',	'He grew up on the wrong side of the garden.',	'Premium',	'Rare',	'Plant'),\
('Gravitree',	'Guardian',	'Fruit Tree Plant',	6,	7,	7,	'Armored 1',	'Whenever a Zombie is played, move it here.',	'The apple doesn\'\'t fall far from the tree. Neither does anything else.',	'Galactic',	'Super-Rare',	'Plant'),\
('Loco Coco',	'Guardian',	'Fruit Nut Plant',	6,	3,	4,	'',	'When played: Make Wall-Nuts next door.\nNut Evolution: All Plants with 0:Strength: get +3:Strength:.',	'He crowned himself King of All Hollow Earth. No one had the heart to tell him it was actually a parliamentary democracy.',	'Triassic',	'Legendary',	'Plant'),\
('Poppin Poppies',	'Guardian',	'Flower Plant',	6,	4,	4,	'',	'When played: Make Lil\'\' Buddies here and next door.',	'Makes friends wherever she goes.',	'Premium',	'Legendary',	'Plant'),\
('Soul Patch',	'Guardian',	'Flower Root Plant',	7,	5,	10,	'Armored 1',	'If your Hero would get hurt, this gets hurt instead.',	'Has been gently encouraging Cherry Bomb and Sour Grapes to attend his meditation class.',	'Premium',	'Legendary',	'Plant'),\
('Wall-Nut Bowling',	'Guardian',	'Nut Trick',	9,	0,	0,	'',	'Make a Wall-Nut in each Ground lane. Attack for 6 damage in those lanes.',	'Ugly shoes not required!',	'Premium',	'Legendary',	'Plant')"

constructor.addToTable(rows)







def pullCardRecord(recordName):
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
		SELECT	name, 
				cardclass.cardclass,
				tribe.tribe, cardtype.cardtype,
				cost, side.side, strength, trait.strengthmodifier, health, trait.healthmodifier,
				trait.trait,
				ability,
				flavor,
				cardset.cardset,
				rarity.rarity
		FROM card
		LEFT JOIN cardtoclass ON card.id = cardtoclass.cardid
		LEFT JOIN cardclass ON cardtoclass.classid = cardclass.id
		LEFT JOIN cardtotrait ON cardtotrait.cardid = card.id
		LEFT JOIN trait ON cardtotrait.traitid = trait.id
		LEFT JOIN cardtotribe ON card.id = cardtotribe.cardid
		LEFT JOIN tribe ON cardtotribe.tribeid = tribe.id
		LEFT JOIN cardtype ON cardtype.id = card.typeid
		LEFT JOIN cardset ON cardset.id = card.setid
		LEFT JOIN rarity ON card.rarityid = rarity.id
		LEFT JOIN side ON card.sideid = side.id
		WHERE card.name = ('%s') ''' % (recordName)

		cursor.execute(join_table_query)
		results = cursor.fetchall()


		print("Printing Table")
		print(results)
		for row in results:
			for col in row:
				temp = col
				print(temp)
			print()

		cardInstance = cardObject(results)
		print(cardInstance.information())

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
		return(cardInstance.information())


