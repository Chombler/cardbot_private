

class cardObject(object):
	record = []
	name = ""
	cardclass = []
	tribes = []
	cardType = ""
	cost = 0
	costModifier = ""
	strength = 0
	strengthModifier = "Strength"
	health = 0
	healthModifier = "Health"
	traits = []
	ability = ""
	flavor = ""
	cardSet = ""
	rarity = ""


	def __init__(self, record):
		self.record = record

		for row in record:
			self.createName(row[0])
			self.createClasses(row[1])
			self.createTribes(row[2])
			self.createType(row[3])
			self.createCost(row[4])
			self.createCostModifier(row[5])
			self.createStrength(row[6])
			self.createStrengthModifier(row[7])
			self.createHealth(row[8])
			self.createHealthModifier(row[9])
			self.createTraits(row[10])
			self.createAbility(row[11])
			self.createFlavor(row[12])
			self.createCardSet(row[13])
			self.createRarity(row[14])

	def createName(self, recordName):
		if(self.name == recordName):
			return
		else:
			self.name = recordName
	
	def createClasses(self, recordClass):
		#print("made it to createClasses")
		if(recordClass in self.cardclass):
			return
		else:
			self.cardclass.append(recordClass)

	def createTribes(self, recordTribe):
		#print("made it to createTribes")
		if(recordTribe is None):
			return
		if(recordTribe in self.tribes):
			return
		else:
			self.tribes.append(recordTribe)

	def createType(self, recordType):
		#print("made it to createType")
		if(self.cardType == recordType):
			return
		else:
			self.cardType = recordType

	def createCost(self, costRecord):
		#print("made it to createCost")
		if(self.cost == costRecord):
			return
		else:
			self.cost = costRecord
	
	def createCostModifier(self, recordCostModifier):
		#print("made it to createCostModifier")
		if(len(self.costModifier) < 1):
			self.costModifier = recordCostModifier
			return
		elif(self.costModifier == recordCostModifier):
			return
		else:
			self.costModifier = "Special"

	def createStrength(self, recordStrength):
		#print("made it to createStrength")
		if(self.strength == recordStrength):
			return
		else:
			self.strength = recordStrength
	
	def createStrengthModifier(self, recordStrengthModifier):
		#print("made it to createStrengthModifier")
		if(recordStrengthModifier is None):
			return
		if(len(self.strengthModifier) < 1):
			self.strengthModifier = recordStrengthModifier
			return
		elif(self.strengthModifier == recordStrengthModifier):
			return
		else:
			self.strengthModifier = "Special"

	
	def createHealth(self, recordHealth):
		#print("made it to createHealth")
		if(self.health == recordHealth):
			return
		else:
			self.health = recordHealth
	
	def createHealthModifier(self, recordHealthModifier):
		#print("made it to createHealthModifier")
		if(recordHealthModifier is None):
			return
		if(len(self.healthModifier) < 1):
			self.healthModifier = recordHealthModifier
			return
		elif(self.healthModifier == recordHealthModifier):
			return
		else:
			self.healthModifier = "Special"
		
	def createTraits(self, recordTrait):
		#print("made it to createTraits")
		if(recordTrait is None):
			return
		if(recordTrait in self.traits):
			return
		else:
			self.traits.append(recordTrait)
	
	def createAbility(self, recordAbility):
		#print("made it to createAbility")
		if(self.ability == recordAbility):
			return
		else:
			self.ability = recordAbility
	

	def createFlavor(self, recordFlavor):
		#print("made it to createFlavor")
		if(self.flavor == recordFlavor):
			return
		else:
			self.flavor = recordFlavor
	
	def createCardSet(self, recordCardSet):
		#print("made it to createCardSet")
		if(recordCardSet is None):
			return
		if(self.cardSet == recordCardSet):
			return
		else:
			self.cardSet = recordCardSet
	
	def createRarity(self, recordRarity):
		#print("made it to createRarity")
		if(self.rarity == recordRarity):
			return
		else:
			self.rarity = recordRarity
	
	def getName(self):
		return(self.name)

	def getClasses(self):
		returnString = ""
		for c in self.cardclass:
			returnString += ":" + c + ":"
		return(returnString)

	def getTribes(self):
		returnString = ""
		for tribe in self.tribes:
			returnString += tribe + " "
		return(returnString)

	def getType(self):
		return(self.cardType)

	def getCost(self):
		return(self.cost)

	def getCostModifier(self):
		return(self.costModifier)

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
				return("%s:%s: %s:%s:/%s:%s:" % (self.cost, self.costModifier, self.strength, self.strengthModifier, self.health, self.healthModifier))
			else:
				return("%s:%s: %s:%s:" % (self.cost, self.costModifier, self.health, self.healthModifier))
		else:
			return("%s:%s:" % (self.cost, self.costModifier))

	def getTraits(self):
		returnString = ""
		for trait in self.traits:
			returnString += trait + " "
		if(len(returnString) > 0):
			returnString += "\n"
		return(returnString)

	def getAbility(self):
		return(self.ability)

	def getFlavor(self):
		return(self.flavor)

	def getSet(self):
		return(self.cardSet + " ")

	def getRarity(self):
		return(self.rarity)

	def information(self):
		return( self.getName() + "\n" +
				self.getClasses() + "\n" +
				self.getTribes() + self.getType() + "\n" +
				self.getStats() + "\n" +
				self.getTraits() +
				self.getAbility() + "\n" +
				self.getFlavor() + "\n" +
				self.getSet() + "-- " + self.getRarity() + " --")



	def __str__(self):
		return self.name


"""
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
