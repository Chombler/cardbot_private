import psycopg2
from psycopg2 import Error
from credentials import token, db_credentials
from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, cardtype, rarity, side, trait, tribe
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
DEFAULT = r"DEFAULT"
print(DEFAULT)

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

trait.addManyToTable(recordTuple)
