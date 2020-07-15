import re as regex


class heroObject(object):
	record = []
	name = ""
	abbreviation = ""
	heroclasses = []
	herosupers = []
	flavor = ""

	def __init__(self, record):
		self.resetCard()
		self.record = record

		for row in record:
			self.createName(row[0])
			self.createAbbreviation(row[1])
			self.createClasses(row[2])
			self.createherosupers(row[3:5])
			self.createFlavor(row[5])

	def resetCard(self):
		self.record = []
		self.name = ""
		self.abbreviation = ""
		self.heroclasses = []
		self.herosupers = []
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
		if(recordSuper[0] in self.herosupers):
			return
		else:
			self.herosupers.append(recordSuper)
		if(recordSuper[1] in self.herosupers[recordSuper[0]]):
			return
		else:
			self.herosupers[recordSuper[0]].append(recordSuper)


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
			returnString += herosuper + "\n"
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
