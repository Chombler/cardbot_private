import re as regex




class heroObject(object):
	record = []
	name = ""
	abbreviation = ""
	heroclasses = []
	herosupers = {}
	flavor = ""
	classSelector = [
	'<:Guardian:286212288334135296>',
	'<:Kabloom:286212306193481729>',
	'<:Mega:286212316632973313>',
	'<:Smarty:286212324996677633>',
	'<:Solar:337606895135358976>',
	'<:Beastly:286212259028533260>',
	'<:Brainy:286212270738898945>',
	'<:Crazy:286212279647731742>',
	'<:Hearty:286212297775644673>',
	'<:Sneaky:286212336379756564>']
	abilitySwitcher = {
	'Strength' : "<:Strength:286215395743105024>",
	'Health' : "<:Health:286215409072603136>",
	'Sun' : "<:Sun:286219730296242186>",
	'Brain' : "<:Brain:286219706883506186>"
	}

	def __init__(self, record):
		self.resetCard()
		self.record = record

		for row in record:
			self.createName(row[0])
			self.createAbbreviation(row[1])
			self.createClasses(row[2])
			self.createherosupers(row[3:6])
			self.createFlavor(row[6])

	def resetCard(self):
		self.record = []
		self.name = ""
		self.abbreviation = ""
		self.heroclasses = []
		self.herosupers = {}
		self.flavor = ""

	def createName(self, recordName):
		self.name = recordName

	def createAbbreviation(self, recordAbbreviation):
		self.abbreviation = recordAbbreviation
	
	def createClasses(self, recordClass):
		if(recordClass in self.heroclasses):
			return
		else:
			self.heroclasses.append(recordClass)

	def createherosupers(self, recordSuper):
		print(recordSuper)
		try:
			if(recordSuper[1] in self.herosupers[recordSuper[0]]):
				pass
			else:
				self.herosupers[recordSuper[0]].append(recordSuper[1])
			if(recordSuper[2] in self.herosupers[recordSuper[0]]):
				pass
			else:
				self.herosupers[recordSuper[0]].append(recordSuper[2])
		except:
			self.herosupers[recordSuper[0]] = [recordSuper[1]]


	def createFlavor(self, recordFlavor):
		self.flavor = recordFlavor
		
	def getName(self):
		return(self.name)

	def getAbbreviation(self):
		return(self.abbreviation)

	def getClasses(self):
		returnString = ""
		for c in self.heroclasses:
			returnString += c
		return(returnString)

	def getherosupers(self):
		returnString = ""
		for herosuper in self.herosupers:
			tempsuper = []
			tempsuperString = ""
			abilityText = ""
			tempsuper.append("**" + herosuper + "** ")
			for superclass in self.herosupers[herosuper]:
				print(superclass)
				if(superclass in self.classSelector):
					tempsuper.append(superclass)
				else:
					abilityText = superclass
					holdText = regex.search('[0123456789 ]\:(.+?)\:', abilityText)
					while(holdText is not None):
						replacement = self.abilitySwitcher.get(holdText.group(1))
						abilityText = abilityText[0:holdText.start()+1] + replacement + abilityText[holdText.end():]
						holdText = regex.search('[0123456789 ]\:(.+?)\:', abilityText)

			tempsuper.append("\n" + abilityText + "\n")
			for entry in tempsuper:
				tempsuperString += entry
			if(tempsuper[2] in self.classSelector):
				returnString = tempsuperString + returnString
			else:
				returnString += tempsuperString

		return(returnString)

	def getFlavor(self):
		return(self.flavor)

	def information(self):
		return( self.getName() + " \{" + self.getAbbreviation() + "\} | " + self.getClasses() + "\n\n" +
				"Supers:\n" + self.getherosupers() +
				"*" + self.getFlavor() + "*\n")


	def __str__(self):
		return self.name


"""
hero_name0, abbreviation1,
cardclass.cardclass2,
card.name3,
hero_flavor4
"""
