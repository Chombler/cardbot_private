import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, cardtype, constructor, cost_type, rarity, nickname, trait, tribe
from cardobject import cardObject
from constructorRows import constructor_rows, nicknameTuple, cardclassTuple, cardsetTuple, cardtypeTuple, cost_typeTuple, rarityTuple, traitTuple, tribeTuple

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

def construct_nickname():
	nickname.dropTable()
	nickname.createTable()
	nickname.addManyToTable(nicknameTuple)
