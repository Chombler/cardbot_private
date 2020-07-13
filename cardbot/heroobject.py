import re as regex


class cardObject(object):
	record = []
	name = ""
	heroclasses = []
	herosupers = []
	flavor = ""

	def __init__(self, record):
		self.resetCard()
		self.record = record

		for row in record:
			self.createName(row[0])
			self.createClasses(row[1])
			self.createherosupers(row[2])
			self.createFlavor(row[3])

	def resetCard(self):
		self.record = []
		self.name = ""
		self.heroclasses = []
		self.herosupers = []
		self.flavor = ""

	def createName(self, recordName):
		self.name = recordName
	
	def createClasses(self, recordClass):
		if(recordClass in self.heroclasses):
			return
		else:
			self.heroclasses.append(recordClass)

	def createherosupers(self, recordSuper):
		if(recordSuper is None):
			return
		if(recordSuper in self.herosupers):
			return
		else:
			self.herosupers.append(recordSuper)

	def createFlavor(self, recordFlavor):
		self.flavor = recordFlavor
		
	def getName(self):
		return(self.name)

	def getClasses(self):
		returnString = ""
		for c in self.heroclasses:
			returnString += c
		return(returnString)

	def getherosupers(self):
		returnString = "- "
		for herosuper in self.herosupers:
			returnString += herosuper + " "
		return(returnString)

	def getFlavor(self):
		return(self.flavor)

	def information(self):
		return( self.getName() + " | " + self.getClasses() + "\n" +
				self.getherosupers() + self.getType() + "\n" +
				"*" + self.getFlavor() + "*\n")


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

"""
