import re as regex


tempString = 'Strikethrough\nPlant Evolution: This gets +3:Strength:.'
text = regex.findall('\n(.+?)\:', tempString)
print('\nAbility text between new line and : is ' + str(text) + '\n')

switcher = {
'Strength' : "<:Strength:286215395743105024>",
'Health' : "<:Health:286215409072603136>",
'Sun' : "<:Sun:286219730296242186>",
'Brain' : "<:Brain:286219706883506186>"
}

emoteString = 'This card attacks with its :Strength: instead of its :Health:.'
abilityText = regex.search('[0123456789 ]\:(.+?)\:', emoteString)
print('Emote text between :s is ' + str(abilityText) + '\n')
print(abilityText.group(1))
print(abilityText.start())
print(abilityText.end())
print(emoteString[abilityText.start()+2:abilityText.end()-1])



holdText = regex.search('[0123456789 ]\:(.+?)\:', emoteString)
while(holdText is not None):
	replacement = switcher.get(holdText.group(1))
	emoteString = emoteString[0:holdText.start()+1] + replacement + emoteString[holdText.end()-1:]
	holdText = regex.search('[0123456789 ]\:(.+?)\:', emoteString)
	
print(emoteString)



"""
recordTuple = [
('Bubble Up',	'Bubble Up'),
('Ensign Uproot',	'Ensign Uproot'),
('FMN',	'Forget-Me-Nuts'),
('Forget-Me-Nuts',	'Forget-Me-Nuts'),
('GC',	'Galacta-Cactus'),
('Gaca',	'Galacta-Cactus'),
('Galacta-Cactus',	'Galacta-Cactus'),
('Garlic',	'Garlic'),
('Grape Responsibility',	'Grape Responsibility'),
('Nut Signal',	'Nut Signal'),
('Photosynthesizer',	'Photosynthesizer'),
('Potato Mine',	'Potato Mine'),
('PPM',	'Primal Potato Mine'),
('Primal Potato Mine',	'Primal Potato Mine'),
('Root Wall',	'Root Wall'),
('Small-Nut',	'Small-Nut'),
('Sting Bean',	'Sting Bean'),
('Wall-Nut',	'Wall-Nut'),
('Cactus',	'Cactus'),
('Corn Dog',	'Corn Dog'),
('Gardening Gloves',	'Gardening Gloves'),
('Grave Buster',	'Grave Buster'),
('Hot Date',	'Hot Date'),
('Jugger-Nut',	'Jugger-Nut'),
('Pismashio',	'Pismashio'),
('Sea-Shroom',	'Sea-Shroom'),
('Spikeweed Sector',	'Spikeweed Sector'),
('Chombler',	'Tricarrotops'),
('Tricarrotops',	'Tricarrotops'),
('Water Chestnut',	'Water Chestnut'),
('Health-Nut',	'Health-Nut'),
('Hibernating Beary',	'Hibernating Beary'),
('Marine Bean',	'Marine Bean'),
('Pea-Nut',	'Pea-Nut'),
('Pear Cub',	'Pear Cub'),
('Plantern',	'Plantern'),
('PWN',	'Primal Wall-Nut'),
('Primal Wall-Nut',	'Primal Wall-Nut'),
('Pumpkin Shell',	'Pumpkin Shell'),
('Shamrocket',	'Shamrocket'),
('Spineapple',	'Spineapple'),
('Steel Magnolia',	'Steel Magnolia'),
('Three-Nut',	'Three-Nut'),
('Blockbuster',	'Blockbuster'),
('Cosmic Nut',	'Cosmic Nut'),
('Force Field',	'Force Field'),
('Guacodile',	'Guacodile'),
('Mirror-Nut',	'Mirror-Nut'),
('Prickly Pear',	'Prickly Pear'),
('Red Stinger',	'Red Stinger'),
('Starch-Lord',	'Starch-Lord'),
('Body-Gourd',	'Body-Gourd'),
('Doom-Shroom',	'Doom-Shroom'),
('Grizzly Pear',	'Grizzly Pear'),
('Pecanolith',	'Pecanolith'),
('Smackadamia',	'Smackadamia'),
('Tough Beets',	'Tough Beets'),
('Gravitree',	'Gravitree'),
('Loco Coco',	'Loco Coco'),
('Poppin Poppies',	'Poppin Poppies'),
('Soul Patch',	'Soul Patch'),
('WNB',	'Wall-Nut Bowling'),
('Wall-Nut Bowling',	'Wall-Nut Bowling'),
('Genetic Amplification',	'Genetic Amplification'),
('Peel Shield',	'Peel Shield'),
('Uncrackable',	'Uncrackable'),
('Puff-Shroom',	'Puff-Shroom'),
('Astro-Shroom',	'Astro-Shroom'),
('Banana Bomb',	'Banana Bomb'),
('Blooming Heart',	'Blooming Heart'),
('Button Mushroom',	'Button Mushroom'),
('HVC',	'High-Voltage Currant'),
('High-Voltage Currant',	'High-Voltage Currant'),
('Hot Lava',	'Hot Lava'),
('Meteor Strike',	'Meteor Strike'),
('More Spore',	'More Spore'),
('Poison Mushroom',	'Poison Mushroom'),
('Reincarnation',	'Reincarnation'),
('Shroom for Two',	'Shroom for Two'),
('S42',	'Shroom for Two'),
('SF2',	'Shroom for Two'),
('SFT',	'Shroom for Two'),
('Storm Front',	'Storm Front'),
('Veloci-Radish Hatchling',	'Veloci-Radish Hatchling'),
('Banana Launcher',	'Banana Launcher'),
('BB',	'Berry Blast'),
('Berry Blast',	'Berry Blast'),
('Buff-Shroom',	'Buff-Shroom'),
('Seedling',	'Seedling'),
('Shelf Mushroom',	'Shelf Mushroom'),
('Wild Berry',	'Wild Berry'),
('Berry Angry',	'Berry Angry'),
('Cosmic Mushroom',	'Cosmic Mushroom'),
('Cro-Magnolia',	'Cro-Magnolia'),
('Imitater',	'Imitater'),
('Invasive Species',	'Invasive Species'),
('Mushroom Grotto',	'Mushroom Grotto'),
('Mushroom Ringleader',	'Mushroom Ringleader'),
('Poison Ivy',	'Poison Ivy'),
('Punish-Shroom',	'Punish-Shroom'),
('Strawberrian',	'Strawberrian'),
('Veloci-Radish Hunter',	'Veloci-Radish Hunter'),
('Zapricot',	'Zapricot'),
('Molekale',	'Molekale'),
('Pair of Pears',	'Pair of Pears'),
('Pair Pearadise',	'Pair Pearadise'),
('Petal-Morphosis',	'Petal-Morphosis'),
('Pineclone',	'Pineclone'),
('Sergeant Strongberry',	'Sergeant Strongberry'),
('Sonic Bloom',	'Sonic Bloom'),
('Sour Grapes',	'Sour Grapes'),
('Transfiguration',	'Transfiguration'),
('Atomic Bombegranate',	'Atomic Bombegranate'),
('Bluesberry',	'Bluesberry'),
('Electric Blueberry',	'Electric Blueberry'),
('Gloom-Shroom',	'Gloom-Shroom'),
('Lava Guava',	'Lava Guava'),
('Sizzle',	'Sizzle'),
('Cherry Bomb',	'Cherry Bomb'),
('Dandy Lion King',	'Dandy Lion King'),
('Poison Oak',	'Poison Oak'),
('GOW',	'Grapes of Wrath'),
('Grapes of Wrath',	'Grapes of Wrath'),
('Kernel Corn',	'Kernel Corn'),
('Tater Toss',	'Tater Toss'),
('Hothead',	'Hothead'),
('Blazing Bark',	'Blazing Bark'),
('Mush-Boom',	'Mush-Boom'),
('Sunburn',	'Sunburn'),
('Banana Peel',	'Banana Peel'),
('Bonk Choy',	'Bonk Choy'),
('Clique Peas',	'Clique Peas'),
('Embiggen',	'Embiggen'),
('Half-Banana',	'Half-Banana'),
('Holo-Flora',	'Holo-Flora'),
('Party Thyme',	'Party Thyme'),
('Pea Pod',	'Pea Pod'),
('Peashooter',	'Peashooter'),
('Sweet Potato',	'Sweet Potato'),
('TTS',	'Time to Shine'),
('Time to Shine',	'Time to Shine'),
('Torchwood',	'Torchwood'),
('Umbrella Leaf',	'Umbrella Leaf'),
('BEP',	'Black-Eyed Pea'),
('Black-Eyed Pea',	'Black-Eyed Pea'),
('Cabbage-Pult',	'Cabbage-Pult'),
('Coffee Grounds',	'Coffee Grounds'),
('Doubled Mint',	'Doubled Mint'),
('Fire Peashooter',	'Fire Peashooter'),
('Lily of the Valley',	'Lily of the Valley'),
('Pea Patch',	'Pea Patch'),
('Split Pea',	'Split Pea'),
('Sweet Pea',	'Sweet Pea'),
('Vegetation Mutation',	'Vegetation Mutation'),
('VM',	'Vegetation Mutation'),
('Cucc',	'Captain Cucumber'),
('Captain Cucumber',	'Captain Cucumber'),
('Cosmic Pea',	'Cosmic Pea'),
('Fertilize',	'Fertilize'),
('Flourish',	'Flourish'),
('Grape Power',	'Grape Power'),
('Grow-Shroom',	'Grow-Shroom'),
('Moonbean',	'Moonbean'),
('Muscle Sprout',	'Muscle Sprout'),
('Podfather',	'Podfather'),
('Repeater',	'Repeater'),
('Typical Beanstalk',	'Typical Beanstalk'),
('Banana Split',	'Banana Split'),
('Bananasaurus Rex',	'Bananasaurus Rex'),
('Plant Food',	'Plant Food'),
('Re-Peat Moss',	'Re-Peat Moss'),
('Savage Spinach',	'Savage Spinach'),
('Skyshooter',	'Skyshooter'),
('Gatling Pea',	'Gatling Pea'),
('Onion Rings',	'Onion Rings'),
('Plucky Clover',	'Plucky Clover'),
('Pod Fighter',	'Pod Fighter'),
('Potted Powerhouse',	'Potted Powerhouse'),
('The Red Plant-It',	'The Red Plant-It'),
('Whipvine',	'Whipvine'),
('Apotatosaurus',	'Apotatosaurus'),
('Bamboozle',	'Bamboozle'),
('Super-Phat Beets',	'Super-Phat Beets'),
('Espresso Fiesta',	'Espresso Fiesta'),
('Power Pummel',	'Power Pummel'),
('Precision Blast',	'Precision Blast'),
('Devour',	'Devour'),
('ANB',	'Admiral Navy Bean'),
('Admiral Navy Bean',	'Admiral Navy Bean'),
('Big Chill',	'Big Chill'),
('Iceberg Lettuce',	'Iceberg Lettuce'),
('Lieutenant Carrotron',	'Lieutenant Carrotron'),
('Lightspeed Seed',	'Lightspeed Seed'),
('Lily Pad',	'Lily Pad'),
('Lima-Pleurodon',	'Lima-Pleurodon'),
('Magic Beanstalk',	'Magic Beanstalk'),
('Mars Flytrap',	'Mars Flytrap'),
('Primal Peashooter',	'Primal Peashooter'),
('Shellery',	'Shellery'),
('Snowdrop',	'Snowdrop'),
('Spyris',	'Spyris'),
('Transmogrify',	'Transmogrify'),
('Weenie Beanie',	'Weenie Beanie'),
('Whirlwind',	'Whirlwind'),
('Bog',	'Bog of Enlightenment'),
('Bog of Enlightenment',	'Bog of Enlightenment'),
('Cosmic Bean',	'Cosmic Bean'),
('Grave Mistake',	'Grave Mistake'),
('Laser Cattail',	'Laser Cattail'),
('Lightning Reed',	'Lightning Reed'),
('Pear Pal',	'Pear Pal'),
('Rotobaga',	'Rotobaga'),
('Snow Pea',	'Snow Pea'),
('Sow Magic Beans',	'Sow Magic Beans'),
('SMB',	'Sow Magic Beans'),
('Cattail',	'Cattail'),
('Chilly Pepper',	'Chilly Pepper'),
('Cool Bean',	'Cool Bean'),
('Go-Nuts',	'Go-Nuts'),
('Mayflower',	'Mayflower'),
('Planet of the Grapes',	'Planet of the Grapes'),
('PotG',	'Planet of the Grapes'),
('Rescue Radish',	'Rescue Radish'),
('Sportacus',	'Sportacus'),
('Spring Bean',	'Spring Bean'),
('Vanilla',	'Vanilla'),
('Bean Counter',	'Bean Counter'),
('Carrotillery',	'Carrotillery'),
('Jelly Bean',	'Jelly Bean'),
('Leaf Blower',	'Leaf Blower'),
('Navy Bean',	'Navy Bean'),
('Sappy Place',	'Sappy Place'),
('Shrinking Violet',	'Shrinking Violet'),
('Snake Grass',	'Snake Grass'),
('Snapdragon',	'Snapdragon'),
('Winter Squash',	'Winter Squash'),
('Witch Hazel',	'Witch Hazel'),
('Bird of Paradise',	'Bird of Paradise'),
('BoP',	'Bird of Paradise'),
('Jolly Holly',	'Jolly Holly'),
('Jumping Bean',	'Jumping Bean'),
('Melon-Pult',	'Melon-Pult'),
('Shooting Starfruit',	'Shooting Starfruit'),
('Smoosh-Shroom',	'Smoosh-Shroom'),
('Threepeater',	'Threepeater'),
('Brainana',	'Brainana'),
('Sap-Fling',	'Sap-Fling'),
('Tricorn',	'Tricorn'),
('Winter Melon',	'Winter Melon'),
('Dark Matter Dragonfruit',	'Dark Matter Dragonfruit'),
('DMD',	'Dark Matter Dragonfruit'),
('The Great Zucchini',	'The Great Zucchini'),
('Goatify',	'Goatify'),
('Lil\'\' Buddy',	'Lil\'\' Buddy'),
('Astrocado Pit',	'Astrocado Pit'),
('Bellflower',	'Bellflower'),
('Cosmoss',	'Cosmoss'),
('Geyser',	'Geyser'),
('Haunted Pumpking',	'Haunted Pumpking'),
('Kernel Pult',	'Kernel Pult'),
('Morning Glory',	'Morning Glory'),
('Primal Sunflower',	'Primal Sunflower'),
('Scorched Earth',	'Scorched Earth'),
('Sunflower',	'Sunflower'),
('Weed Whack',	'Weed Whack'),
('Apple-Saucer',	'Apple-Saucer'),
('Eyespore',	'Eyespore'),
('Fume-Shroom',	'Fume-Shroom'),
('Pepper M.D.',	'Pepper M.D.'),
('Sage Sage',	'Sage Sage'),
('Sun-Shroom',	'Sun-Shroom'),
('Twin Sunflower',	'Twin Sunflower'),
('Water Balloons',	'Water Balloons'),
('2nd-Best Taco of All Time',	'2nd-Best Taco of All Time'),
('Cosmic Flower',	'Cosmic Flower'),
('Jack O\'\' Lantern',	'Jack O\'\' Lantern'),
('Ketchup Mechanic',	'Ketchup Mechanic'),
('Magnifying Grass',	'Magnifying Grass'),
('Mixed Nuts',	'Mixed Nuts'),
('Solar Winds',	'Solar Winds'),
('Sunflower Seed',	'Sunflower Seed'),
('Sunnier-Shroom',	'Sunnier-Shroom'),
('Venus Flytrap',	'Venus Flytrap'),
('Whack-a-Zombie',	'Whack-a-Zombie'),
('Bloomerang',	'Bloomerang'),
('Chomper',	'Chomper'),
('Elderberry',	'Elderberry'),
('Heartichoke',	'Heartichoke'),
('Lawnmower',	'Lawnmower'),
('Metal Petal Sunflower',	'Metal Petal Sunflower'),
('Sun Strike',	'Sun Strike'),
('Venus Flytraplanet',	'Venus Flytraplanet'),
('Wing-Nut',	'Wing-Nut'),
('Aloesaurus',	'Aloesaurus'),
('Astrocado',	'Astrocado'),
('Briar Rose',	'Briar Rose'),
('Power Flower',	'Power Flower'),
('Squash',	'Squash'),
('Cob Cannon',	'Cob Cannon'),
('Laser Bean',	'Laser Bean'),
('Smashing Pumpkin',	'Smashing Pumpkin'),
('Tactical Cuke',	'Tactical Cuke'),
('3HC',	'Three-Headed Chomper'),
('THC',	'Three-Headed Chomper'),
('Three-Headed Chomper',	'Three-Headed Chomper'),
('Toadstool',	'Toadstool'),
('Astro Vera',	'Astro Vera'),
('Cornucopia',	'Cornucopia'),
('Goat',	'Goat'),
('Acid Rain',	'Acid Rain'),
('Cat Lady',	'Cat Lady'),
('Cheese Cutter',	'Cheese Cutter'),
('Dog Walker',	'Dog Walker'),
('Evaporate',	'Evaporate'),
('Fraidy Cat',	'Fraidy Cat'),
('Galvanize',	'Galvanize'),
('Nibble',	'Nibble'),
('Secret Agent',	'Secret Agent'),
('Skunk Punk',	'Skunk Punk'),
('Snorkel Zombie',	'Snorkel Zombie'),
('Yeti Lunchbox',	'Yeti Lunchbox'),
('Biodome Botanist',	'Biodome Botanist'),
('Cyborg Zombie',	'Cyborg Zombie'),
('Energy Drink Zombie',	'Energy Drink Zombie'),
('Extinction Event',	'Extinction Event'),
('Haunting Ghost',	'Haunting Ghost'),
('Haunting Zombie',	'Haunting Zombie'),
('Hunting Grounds',	'Hunting Grounds'),
('Killer Whale',	'Killer Whale'),
('Pied Piper',	'Pied Piper'),
('Squirrel Herder',	'Squirrel Herder'),
('Synchronized Swimmer',	'Synchronized Swimmer'),
('Total Eclipse',	'Total Eclipse'),
('Zookeeper',	'Zookeeper'),
('Alien Ooze',	'Alien Ooze'),
('Area 22',	'Area 22'),
('A22',	'Area 22'),
('Dolphin Rider',	'Dolphin Rider'),
('Hover-Goat 3000',	'Hover-Goat 3000'),
('Loudmouth',	'Loudmouth'),
('Vimpire',	'Vimpire'),
('Vitamin Z',	'Vitamin Z'),
('Zombie Yeti',	'Zombie Yeti'),
('Ancient Vimpire',	'Ancient Vimpire'),
('B-Flat',	'B-Flat'),
('Cosmic Yeti',	'Cosmic Yeti'),
('Interstellar Bounty Hunter',	'Interstellar Bounty Hunter'),
('IBH',	'Interstellar Bounty Hunter'),
('Kangaroo Rider',	'Kangaroo Rider'),
('Overstuffed Zombie',	'Overstuffed Zombie'),
('Primordial Cheese Shover',	'Primordial Cheese Shover'),
('Sneezing Zombie',	'Sneezing Zombie'),
('Surfer Zombie',	'Surfer Zombie'),
('Locust Swarm',	'Locust Swarm'),
('Mondo Bronto',	'Mondo Bronto'),
('Smashing Gargantuar',	'Smashing Gargantuar'),
('Supernova Gargantuar',	'Supernova Gargantuar'),
('Vengeful Cyborg',	'Vengeful Cyborg'),
('Deep Sea Gargantuar',	'Deep Sea Gargantuar'),
('King of the Grill',	'King of the Grill'),
('Maniacal Laugh',	'Maniacal Laugh'),
('GTG',	'Gargantuar-Throwing Gargantuar'),
('Gargantuar-Throwing Gargantuar',	'Gargantuar-Throwing Gargantuar'),
('Nurse Gargantuar',	'Nurse Gargantuar'),
('Octo Zombie',	'Octo Zombie'),
('Zombot 1000',	'Zombot 1000'),
('Stayin\'\' Alive',	'Stayin\'\' Alive'),
('Cardboard Robot Zombie',	'Cardboard Robot Zombie'),
('Chimney Sweep',	'Chimney Sweep'),
('Cut Down to Size',	'Cut Down to Size'),
('Interdimensional Zombie',	'Interdimensional Zombie'),
('IDZ',	'Interdimensional Zombie'),
('Iron Boarder',	'Iron Boarder'),
('Leprechaun Imp',	'Leprechaun Imp'),
('Mustache Waxer',	'Mustache Waxer'),
('Neutron Imp',	'Neutron Imp'),
('Paparazzi Zombie',	'Paparazzi Zombie'),
('Pot of Gold',	'Pot of Gold'),
('Summoning',	'Summoning'),
('Telepathy',	'Telepathy'),
('Teleport',	'Teleport'),
('Teleportation Station',	'Teleportation Station'),
('Beam Me Up',	'Beam Me Up'),
('BMU',	'Beam Me Up'),
('Cell Phone Zombie',	'Cell Phone Zombie'),
('Cosmic Scientist',	'Cosmic Scientist'),
('Cryo-Brain',	'Cryo-Brain'),
('Evolutionary Leap',	'Evolutionary Leap'),
('Lurch for Lunch',	'Lurch for Lunch'),
('Pool Shark',	'Pool Shark'),
('Space Cadet',	'Space Cadet'),
('Teleportation Zombie',	'Teleportation Zombie'),
('Transformation Station',	'Transformation Station'),
('Zombot Drone Engineer',	'Zombot Drone Engineer'),
('Brain Vendor',	'Brain Vendor'),
('Duckstache',	'Duckstache'),
('Electrician',	'Electrician'),
('Fun-Dead Raiser',	'Fun-Dead Raiser'),
('Gentleman Zombie',	'Gentleman Zombie'),
('Kite Flyer',	'Kite Flyer'),
('Medulla Nebula',	'Medulla Nebula'),
('Moonwalker',	'Moonwalker'),
('MM',	'Mustache Monument'),
('Mustache Monument',	'Mustache Monument'),
('Regifting Zombie',	'Regifting Zombie'),
('Rocket Science',	'Rocket Science'),
('ToT',	'Trick-or-Treater'),
('Trick-or-Treater',	'Trick-or-Treater'),
('Wormhole Gatekeeper',	'Wormhole Gatekeeper'),
('Zom-Blob',	'Zom-Blob'),
('Drum Major',	'Drum Major'),
('Mad Chemist',	'Mad Chemist'),
('Mountain Climber',	'Mountain Climber'),
('Parasol Zombie',	'Parasol Zombie'),
('Thinking Cap',	'Thinking Cap'),
('Triplication',	'Triplication'),
('Copter Commando',	'Copter Commando'),
('Gadget Scientist',	'Gadget Scientist'),
('Gargantuar Mime',	'Gargantuar Mime'),
('Pirate\'\'s Booty',	'Pirate\'\'s Booty'),
('Portal Technician',	'Portal Technician'),
('Shieldcrusher Viking',	'Shieldcrusher Viking'),
('Hail-a-Copter',	'Hail-a-Copter'),
('Kitchen Sink Zombie',	'Kitchen Sink Zombie'),
('Wizard Gargantuar',	'Wizard Gargantuar'),
('Bad Moon Rising',	'Bad Moon Rising'),
('BMR',	'Bad Moon Rising'),
('Zombot Dinotronic Mechasaur',	'Zombot Dinotronic Mechasaur'),
('Trickster',	'Trickster'),
('Witch\'\'s Familiar',	'Witch\'\'s Familiar'),
('Zom-Bats',	'Zom-Bats'),
('Eureka',	'Eureka'),
('Shrink Ray',	'Shrink Ray'),
('Carried Away',	'Carried Away'),
('Terror-Former 10,000',	'Terror-Former 10,000'),
('Backup Dancer',	'Backup Dancer'),
('Brute Strength',	'Brute Strength'),
('Bungee Plumber',	'Bungee Plumber'),
('Dance Off',	'Dance Off'),
('Disco-Naut',	'Disco-Naut'),
('Electrobolt',	'Electrobolt'),
('Grave Robber',	'Grave Robber'),
('Loose Cannon',	'Loose Cannon'),
('Mystery Egg',	'Mystery Egg'),
('Quickdraw Con Man',	'Quickdraw Con Man'),
('Tennis Champ',	'Tennis Champ'),
('Trapper Territory',	'Trapper Territory'),
('Unlife of the Party',	'Unlife of the Party'),
('Aerobics Instructor',	'Aerobics Instructor'),
('BoD',	'Barrel of Deadbeards'),
('Barrel of Deadbeards',	'Barrel of Deadbeards'),
('Conga Zombie',	'Conga Zombie'),
('Cuckoo Zombie',	'Cuckoo Zombie'),
('Disco Dance Floor',	'Disco Dance Floor'),
('DDF',	'Dsco Dance Floor'),
('Exploding Fruitcake',	'Exploding Fruitcake'),
('Final Mission',	'Final Mission'),
('Meteor Z',	'Meteor Z'),
('Newspaper Zombie',	'Newspaper Zombie'),
('Quasar Wizard',	'Quasar Wizard'),
('Space Ninja',	'Space Ninja'),
('Sugary Treat',	'Sugary Treat'),
('Zombie\'\'s Best Friend',	'Zombie\'\'s Best Friend'),
('Abracadaver',	'Abracadaver'),
('Captain Deadbeard',	'Captain Deadbeard'),
('Disco Zombie',	'Disco Zombie'),
('Exploding Imp',	'Exploding Imp'),
('Fireworks Zombie',	'Fireworks Zombie'),
('Gizzard Lizard',	'Gizzard Lizard'),
('Jester',	'Jester'),
('Moon Base Z',	'Moon Base Z'),
('Unexpected Gifts',	'Unexpected Gifts'),
('Zombot\'\'s Wrath',	'Zombot\'\'s Wrath'),
('Cakesplosion',	'Cakesplosion'),
('Cosmic Dancer',	'Cosmic Dancer'),
('HH',	'Headhunter'),
('Headhunter',	'Headhunter'),
('Orchestra Conductor',	'Orchestra Conductor'),
('Stupid Cupid',	'Stupid Cupid'),
('Tankylosaurus',	'Tankylosaurus'),
('The Chickening',	'The Chickening'),
('Valkyrie',	'Valkyrie'),
('Binary Stars',	'Binary Stars'),
('Flamenco Zombie',	'Flamenco Zombie'),
('Foot Soldier Zombie',	'Foot Soldier Zombie'),
('Frankentaur',	'Frankentaur'),
('GTI',	'Gargantuar-Throwing Imp'),
('Gargantuar-Throwing Imp',	'Gargantuar-Throwing Imp'),
('Hippity Hop Gargantuar',	'Hippity Hop Gargantuar'),
('ITG',	'Imp-Throwing Gargantuar'),
('Imp-Throwing Gargantuar',	'Imp-Throwing Gargantuar'),
('Disco-Tron 3000',	'Disco-Tron 3000'),
('Gas Giant',	'Gas Giant'),
('Gargantuars\'\' Feast',	'Gargantuars\'\' Feast'),
('Arm Wrestler',	'Arm Wrestler'),
('Baseball Zombie',	'Baseball Zombie'),
('Black Hole',	'Black Hole'),
('Camel Crossing',	'Camel Crossing'),
('Genetic Experiment',	'Genetic Experiment'),
('Healthy Treat',	'Healthy Treat'),
('Heroic Health',	'Heroic Health'),
('Planetary Gladiator',	'Planetary Gladiator'),
('Possessed',	'Possessed'),
('Rock Wall',	'Rock Wall'),
('Rolling Stone',	'Rolling Stone'),
('Zombie Middle Manager',	'Zombie Middle Manager'),
('Zombology Teacher',	'Zombology Teacher'),
('Cone Zone',	'Cone Zone'),
('Conehead',	'Conehead'),
('ETT',	'Escape through Time'),
('Escape through Time',	'Escape through Time'),
('Flag Zombie',	'Flag Zombie'),
('Gargologist',	'Gargologist'),
('Jurassic Fossilhead',	'Jurassic Fossilhead'),
('Leftovers',	'Leftovers'),
('Sumo Wrestler',	'Sumo Wrestler'),
('Terrify',	'Terrify'),
('Turkey Rider',	'Turkey Rider'),
('Celestial Custodian',	'Celestial Custodian'),
('Cosmic Sports Star',	'Cosmic Sports Star'),
('Going Viral',	'Going Viral'),
('GV',	'Going Viral'),
('Knockout',	'Knockout'),
('Landscaper',	'Landscaper'),
('Lost Colosseum',	'Lost Colosseum'),
('Team Mascot',	'Team Mascot'),
('Trash Can Zombie',	'Trash Can Zombie'),
('Weed Spray',	'Weed Spray'),
('Bonus Track Buckethead',	'Bonus Track Buckethead'),
('Buckethead',	'Buckethead'),
('Medic',	'Medic'),
('Stompadon',	'Stompadon'),
('Turquoise Skull Zombie',	'Turquoise Skull Zombie'),
('Zombie Coach',	'Zombie Coach'),
('Zombie King',	'Zombie King'),
('All-Star Zombie',	'All-Star Zombie'),
('Chum Champion',	'Chum Champion'),
('Intergalactic Warlord',	'Intergalactic Warlord'),
('Monster Mash',	'Monster Mash'),
('Primeval Yeti',	'Primeval Yeti'),
('Screen Door Zombie',	'Screen Door Zombie'),
('Coffee Zombie',	'Coffee Zombie'),
('Defensive End',	'Defensive End'),
('Ra Zombie',	'Ra Zombie'),
('Undying Pharoah',	'Undying Pharoah'),
('Zombot Battlecruiser 5000',	'Zombot Battlecruiser 5000'),
('Knight of the Living Dead',	'Knight of the Living Dead'),
('Rodeo Gargantuar',	'Rodeo Gargantuar'),
('Wannabe Hero',	'Wannabe Hero'),
('Slammin\'\' Smackdown',	'Slammin\'\' Smackdown'),
('Missle Madness',	'Missle Madness'),
('Octo-Pult',	'Octo-Pult'),
('Octo-Pet',	'Octo-Pet'),
('Swabbie',	'Swabbie'),
('Buried Treasure',	'Buried Treasure'),
('Dolphinado',	'Dolphinado'),
('Ducky Tube Zombie',	'Ducky Tube Zombie'),
('Graveyard',	'Graveyard'),
('Headstone Carver',	'Headstone Carver'),
('Ice Moon',	'Ice Moon'),
('Imp',	'Imp'),
('Imposter',	'Imposter'),
('In-Crypted',	'In-Crypted'),
('Mini-Ninja',	'Mini-Ninja'),
('Smoke Bomb',	'Smoke Bomb'),
('Super Stench',	'Super Stench'),
('Zombie Chicken',	'Zombie Chicken'),
('Barrel of Barrels',	'Barrel of Barrels'),
('BoB',	'Barrel of Barrels'),
('Dr. Spacetime',	'Dr. Spacetime'),
('Fire Rooster',	'Fire Rooster'),
('Fishy Imp',	'Fishy Imp'),
('Frosty Mustache',	'Frosty Mustache'),
('Hot Dog Imp',	'Hot Dog Imp'),
('Ice Pirate',	'Ice Pirate'),
('ITI',	'Imp-Throwing Imp'),
('Imp-Throwing Imp',	'Imp-Throwing Imp'),
('Monkey Smuggler',	'Monkey Smuggler'),
('Smelly Zombie',	'Smelly Zombie'),
('Main Pirate',	'Swashbuckler Zombie'),
('Swashbuckler Zombie',	'Swashbuckler Zombie'),
('TWI',	'Toxic Waste Imp'),
('Toxic Waste Imp',	'Toxic Waste Imp'),
('Backyard Bounce',	'Backyard Bounce'),
('Captain Flameface',	'Captain Flameface'),
('Cosmic Imp',	'Cosmic Imp'),
('Excavator Zombie',	'Excavator Zombie'),
('Imp Commander',	'Imp Commander'),
('Laser Base Alpha',	'Laser Base Alpha'),
('LBA',	'Laser Base Alpha'),
('Line Dancing Zombie',	'Line Dancing Zombie'),
('Raiding Raptor',	'Raiding Raptor'),
('Space Pirate',	'Space Pirate'),
('Stealthy Imp',	'Stealthy Imp'),
('Zombie High Diver',	'Zombie High Diver'),
('Barrel Roller Zombie',	'Barrel Roller Zombie'),
('Firefighter',	'Firefighter'),
('Pogo Bouncer',	'Pogo Bouncer'),
('Space Cowboy',	'Space Cowboy'),
('Tomb Raiser Zombie',	'Tomb Raiser Zombie'),
('Trapper Zombie',	'Trapper Zombie'),
('Unthawed Viking',	'Unthawed Viking'),
('Blowgun Imp',	'Blowgun Imp'),
('Cryo-Yeti',	'Cryo-Yeti'),
('Mixed-Up Gravedigger',	'Mixed-Up Gravedigger'),
('MuG',	'Mixed-Up Gravedigger'),
('Surprise Gargantuar',	'Surprise Gargantuar'),
('Walrus Rider',	'Walrus Rider'),
('Cursed Gargolith',	'Cursed Gargolith'),
('Zombot Aerostatic Gondola',	'Zombot Aerostatic Gondola'),
('Zombot Sharktronic Sub',	'Zombot Sharktronic Sub'),
('Zombot Stomp',	'Zombot Stomp'),
('Zombot Plank Walker',	'Zombot Plank Walker'),
('Frozen Tundra',	'Frozen Tundra'),
('Impfinity Clone',	'Impfinity Clone'),
('Triple Threat',	'Triple Threat')]

nickname.dropTable()
nickname.createTable()
nickname.addManyToTable(recordTuple)

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
('<:Guardian:286212288334135296>',),
('<:Kabloom:286212306193481729>',),
('<:Mega:286212316632973313>',),
('<:Smarty:286212324996677633>',),
('<:Solar:337606895135358976>',),
('<:Beastly:286212259028533260>',),
('<:Brainy:286212270738898945>',),
('<:Crazy:286212279647731742>',),
('<:Hearty:286212297775644673>',),
('<:Sneaky:286212336379756564>',)]

cardclass.dropTable()
cardclass.createTable()
cardclass.addManyToTable(recordTuple)

recordTuple = [
('Basic',),
('Premium',),
('Galactic',),
('Colossal',),
('Triassic',)]

cardset.createTable()
cardset.addManyToTable(recordTuple)

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
('<:Sun:286219730296242186>',),
('<:Brain:286219706883506186>',)]

side.dropTable()
side.createTable()
side.addManyToTable(recordTuple)


recordTuple = [
('Amphibious', None, None),
('Anti-Hero 2', '<:AntiHero:286216212831141888>', None),
('Anti-Hero 3', '<:AntiHero:286216212831141888>', None),
('Anti-Hero 4', '<:AntiHero:286216212831141888>', None),
('Anti-Hero 5', '<:AntiHero:286216212831141888>', None),
('Armored 1', None, '<:Armored:286220300763529216>'),
('Armored 2', None, '<:Armored:286220300763529216>'),
('Bullseye', '<:Bullseye:286215435400118272> ', None),
('Deadly', '<:Deadly:286214530155937792> ', None),
('Double Strike', '<:DoubleStrike:331848241488461826> ', None),
('Hunt', None, None),
('Frenzy', '<:Frenzy:286212444332883970> ', None),
('Gravestone', None, None),
('HealthStrength', None, '<:healthstrength:289224527995600897> '),
('Overshoot 2', '<:Overshoot:326761366700556290> ', None),
('Overshoot 3', '<:Overshoot:326761366700556290> ', None),
('Splash Damage 1', None, None),
('Splash Damage 3', None, None),
('Splash Damage 6', None, None),
('Strikethrough', '<:Strikethrough:286214542264893453> ', None),
('Team-Up', None, None),
('Untrickable', None, '<:Untrickable:350385647439314945>')]

trait.dropTable()
trait.createTable()
trait.addManyToTable(recordTuple)

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




multiAddToTable()
card.createTable()
cardclass.createTable()
cardset.createTable()
cardtoclass.createTable()
cardtotrait.createTable()
cardtotribe.createTable()
rarity.createTable()
side.createTable()
trait.createTable()
tribe.createTable()
card.addToTable((1, 'Forget-Me-Nuts',	1,	2,	1,	'Zombie tricks cost 1:Brain: more.',	'\"I\'d forget my own flower if it wasn\'t stuck to my head. Wait, what were we talking about?\"',	NULL,	0,	1))

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
	WHERE card.id = 1
	'''

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

=SWITCH(C3, REGEXMATCH(C3, AB2), "("+A2+", " + AA2 + ")", REGEXMATCH(C3, AB3), "("+A2+", " + AA3 + ")", REGEXMATCH(C3, AB4), "("+A2+", " + AA4 + ")", REGEXMATCH(C3, AB5), "("+A2+", " + AA5 + ")", REGEXMATCH(C3, AB6), "("+A2+", " + AA6 + ")", REGEXMATCH(C3, AB7), "("+A2+", " + AA7 + ")", REGEXMATCH(C3, AB8), "("+A2+", " + AA8 + ")", REGEXMATCH(C3, AB9), "("+A2+", " + AA9 + ")", REGEXMATCH(C3, AB810), "("+A2+", " + AA10 + ")", REGEXMATCH(C3, AB11), "("+A2+", " + AA11 + ")", REGEXMATCH(C3, AB12), "("+A2+", " + AA12 + ")", REGEXMATCH(C3, AB13), "("+A2+", " + AA13 + ")", REGEXMATCH(C3, AB14), "("+A2+", " + AA14 + ")", REGEXMATCH(C3, AB15), "("+A2+", " + AA15 + ")", REGEXMATCH(C3, AB16), "("+A2+", " + AA16 + ")", REGEXMATCH(C3, AB17), "("+A2+", " + AA17 + ")", REGEXMATCH(C3, AB18), "("+A2+", " + AA18 + ")", REGEXMATCH(C3, AB19), "("+A2+", " + AA19 + ")", REGEXMATCH(C3, AB20), "("+A2+", " + AA20 + ")", REGEXMATCH(C3, AB21), "("+A2+", " + AA21 + ")", REGEXMATCH(C3, AB22), "("+A2+", " + AA22 + ")", REGEXMATCH(C3, AB23), "("+A2+", " + AA23 + ")", REGEXMATCH(C3, AB24), "("+A2+", " + AA24 + ")", REGEXMATCH(C3, AB25), "("+A2+", " + AA25 + ")", REGEXMATCH(C3, AB26), "("+A2+", " + AA26 + ")", REGEXMATCH(C3, AB27), "("+A2+", " + AA27 + ")", REGEXMATCH(C3, AB28), "("+A2+", " + AA28 + ")", REGEXMATCH(C3, AB29), "("+A2+", " + AA29 + ")", REGEXMATCH(C3, AB30), "("+A2+", " + AA30 + ")", REGEXMATCH(C3, AB31), "("+A2+", " + AA31 + ")", REGEXMATCH(C3, AB32), "("+A2+", " + AA32 + ")", REGEXMATCH(C3, AB33), "("+A2+", " + AA33 + ")", REGEXMATCH(C3, AB34), "("+A2+", " + AA34 + ")", REGEXMATCH(C3, AB35), "("+A2+", " + AA35 + ")", REGEXMATCH(C3, AB36), "("+A2+", " + AA36 + ")", REGEXMATCH(C3, AB37), "("+A2+", " + AA37 + ")", REGEXMATCH(C3, AB38), "("+A2+", " + AA38 + ")", "")


constructor.addToTable(rows)


"""