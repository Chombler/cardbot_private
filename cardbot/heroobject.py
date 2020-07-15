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
			superability = ""
			returnString += "**" + herosuper + "** "
			for superclass in self.herosupers[herosuper]:
				if(superclass in self.classSelector):
					returnString += superclass
				else:
					superability = superclass
			returnString += "\n" + superability + "\n"
		return(returnString)

	def getFlavor(self):
		return(self.flavor)

	def information(self):
		return( self.getName() + " \{" + self.getAbbreviation() + "\} | " + self.getClasses() + "\n" +
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
