import re as regex


class cardObject(object):
	record = []
	name = ""
	cardclass = []
	tribes = []
	cardType = ""
	cost = 0
	costType = ""
	strength = 0
	strengthModifier = "<:Strength:286215395743105024>"
	health = 0
	healthModifier = "<:Health:286215409072603136>"
	traits = []
	ability = ""
	flavor = ""
	cardSet = ""
	rarity = ""
	abilitySwitcher = {
	'Strength' : "<:Strength:286215395743105024>",
	'Health' : "<:Health:286215409072603136>",
	'Sun' : "<:Sun:286219730296242186>",
	'Brain' : "<:Brain:286219706883506186>"
	}

	traitSwitcher = {
	'Amphibious' : '',
	'Anti-Hero 2': '<:AntiHero:286216212831141888>',
	'Anti-Hero 3': '<:AntiHero:286216212831141888>',
	'Anti-Hero 4': '<:AntiHero:286216212831141888>',
	'Anti-Hero 5': '<:AntiHero:286216212831141888>',
	'Armored 1': '<:Armored:286220300763529216>',
	'Armored 2': '<:Armored:286220300763529216>',
	'Bullseye': '<:Bullseye:286215435400118272>',
	'Deadly': '<:Deadly:286214530155937792>',
	'Double Strike': '<:DoubleStrike:331848241488461826>',
	'Hunt': '',
	'Frenzy': '<:Frenzy:286212444332883970>',
	'Gravestone': '',
	'Overshoot 2': '<:Overshoot:326761366700556290>',
	'Overshoot 3': '<:Overshoot:326761366700556290>',
	'Splash Damage 1': '',
	'Splash Damage 3': '',
	'Splash Damage 6': '',
	'Strikethrough': '<:Strikethrough:286214542264893453>',
	'Team-Up': '',
	'Untrickable': '<:Untrickable:350385647439314945>'
	}


	def __init__(self, record):
		self.resetCard()
		self.record = record

		for row in record:
			self.createName(row[0])
			self.createClasses(row[1])
			self.createTribes(row[2])
			self.createType(row[3])
			self.createCost(row[4])
			self.createCostType(row[5])
			self.createStrength(row[6])
			self.createStrengthModifier(row[7])
			self.createHealth(row[8])
			self.createHealthModifier(row[9])
			self.createTraits(row[10])
			self.createAbility(row[11])
			self.createFlavor(row[12])
			self.createCardSet(row[13])
			self.createRarity(row[14])

	def resetCard(self):
		self.record = []
		self.name = ""
		self.cardclass = []
		self.tribes = []
		self.cardType = ""
		self.cost = 0
		self.costType = ""
		self.strength = 0
		self.strengthModifier = "<:Strength:286215395743105024>"
		self.health = 0
		self.healthModifier = "<:Health:286215409072603136>"
		self.traits = []
		self.ability = ""
		self.flavor = ""
		self.cardSet = ""
		self.rarity = ""


	def createName(self, recordName):
		self.name = recordName
	
	def createClasses(self, recordClass):
		if(recordClass in self.cardclass):
			return
		else:
			self.cardclass.append(recordClass)

	def createTribes(self, recordTribe):
		if(recordTribe is None):
			return
		if(recordTribe in self.tribes):
			return
		else:
			self.tribes.append(recordTribe)

	def createType(self, recordType):
		self.cardType = recordType

	def createCost(self, costRecord):
		self.cost = costRecord
	
	def createCostType(self, recordCostType):
		if(len(self.costType) < 1):
			self.costType = recordCostType
			return
		elif(self.costType == recordCostType):
			return
		else:
			self.costType = "Special"

	def createStrength(self, recordStrength):
		self.strength = recordStrength
	
	def createStrengthModifier(self, recordStrengthModifier):
		if(recordStrengthModifier is None):
			return
		if(self.strengthModifier == recordStrengthModifier):
			return
		self.strengthModifier = recordStrengthModifier if self.strengthModifier == "<:Strength:286215395743105024>" else "<:Special:291347137365540864>"

	
	def createHealth(self, recordHealth):
		self.health = recordHealth if self.health != recordHealth else self.health
	
	def createHealthModifier(self, recordHealthModifier):
		if(recordHealthModifier is None):
			return
		if(self.healthModifier == recordHealthModifier):
			return
		self.healthModifier = recordHealthModifier if self.healthModifier == "<:Health:286215409072603136>" else "<:Special:291347137365540864>"
		
	def createTraits(self, recordTrait):
		if(recordTrait is None):
			return
		if(recordTrait == 'HealthStrength'):
			return
		if(recordTrait in self.traits):
			return
		else:
			self.traits.append(recordTrait)
	
	def createAbility(self, recordAbility):
		self.ability = recordAbility

	def createFlavor(self, recordFlavor):
		self.flavor = recordFlavor
	
	def createCardSet(self, recordCardSet):
		if(recordCardSet is None):
			return
		self.cardSet = recordCardSet
	
	def createRarity(self, recordRarity):
		self.rarity = recordRarity
	
	def getName(self):
		return(self.name)

	def getClasses(self):
		returnString = ""
		for c in self.cardclass:
			returnString += c
		return(returnString)

	def getTribes(self):
		returnString = "- "
		for tribe in self.tribes:
			returnString += tribe + " "
		return(returnString)

	def getType(self):
		return(self.cardType + " -")

	def getCost(self):
		return(self.cost)

	def getCostType(self):
		return(self.CostType)

	def getStrength(self):
		return(self.strength)

	def getStrengthModifier(self):
		return(self.strengthModifier)

	def getHealth(self):
		return(self.health)

	def getHealthModifier(self):
		return(self.healthModifier)

	def getStats(self):
		if(self.health != 0):
			if(self.strength != 0):
				return("%s%s %s%s/%s%s" % (self.cost, self.costType, self.strength, self.strengthModifier, self.health, self.healthModifier))
			else:
				return("%s%s %s%s" % (self.cost, self.costType, self.health, self.healthModifier))
		else:
			return("%s%s" % (self.cost, self.costType))

	def getTraits(self):
		returnString = ""
		for trait in self.traits:
			returnString += self.traitSwitcher.get(trait) + "__" + trait + "__, "
		else:
			returnString = returnString[0:-2]
		returnString += "\n" if len(returnString) > 0 else ""
		return(returnString)

	def getAbility(self):
		abilityText = self.ability + "\n" if len(self.ability) > 0 else ""
		holdText = regex.search('[0123456789 ]\:(.+?)\:', abilityText)
		while(holdText is not None):
			replacement = self.abilitySwitcher.get(holdText.group(1))
			abilityText = abilityText[0:holdText.start()+1] + replacement + abilityText[holdText.end():]
			holdText = regex.search('[0123456789 ]\:(.+?)\:', abilityText)

		return(abilityText)

	def getFlavor(self):
		return(self.flavor)

	def getSet(self):
		return(self.cardSet + " - " if len(self.cardSet) > 0 else "")

	def getRarity(self):
		return(self.rarity)

	def information(self):
		return( self.getName() + " | " + self.getClasses() + "\n" +
				self.getTribes() + self.getType() + "\n" +
				self.getStats() + "\n" +
				self.getTraits() +
				self.getAbility() + 
				"*" + self.getFlavor() + "*\n" +
				"**\<\< " + (self.getSet() + self.getRarity()).upper() + " \>\>**")



	def __str__(self):
		return self.name


"""


<:Strength:286215395743105024> 
<:Health:286215409072603136> 
<:Sun:286219730296242186> 
<:Brain:286219706883506186> 
<:Guardian:286212288334135296> 
<:Kabloom:286212306193481729> 
<:Mega:286212316632973313> 
<:Smarty:286212324996677633> 
<:Solar:337606895135358976> 
<:Beastly:286212259028533260> 
<:Brainy:286212270738898945> 
<:Crazy:286212279647731742> 
<:Hearty:286212297775644673> 
<:Sneaky:286212336379756564> 
<:AntiHero:286216212831141888> 
<:Armored:286220300763529216> 
<:Bullseye:286215435400118272> 
<:Deadly:286214530155937792> 
<:DoubleStrike:331848241488461826> 
<:Frenzy:286212444332883970> 
<:healthstrength:289224527995600897> 
<:Overshoot:326761366700556290> 
<:Special:291347137365540864> 
<:Strikethrough:286214542264893453> 
<:Untrickable:350385647439314945>

0name, 
1cardclass.cardclass,
2tribe.tribe, 3cardtype.cardtype,
4cost, 5side.side, 6strength, 7trait.strengthmodifier, 8health, 9trait.healthmodifier,
10trait.trait,
11ability,
12flavor,
13cardset.cardset,
14rarity.rarity
"""
