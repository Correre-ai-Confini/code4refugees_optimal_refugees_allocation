class Tent:
	def __init__(self, **kwargs):
		self.id = kwargs['id'] #string
		self.maxSpace = kwargs['maxSpace'] #integer
		self.occupants = kwargs['occupants'] #array(Occupant)
		self.distanceFromMed = kwargs['distanceFromMed'] #float [0,1]
		
	def getAvailableSpace(self):
		return ( self.maxSpace - len(self.occupants) )
		
	def getNumGender(self, gender):
		result=0
		for individual in self.occupants :
			if(individual.gender == gender) : result += 1
		return result
		
	#etc. for other features.
	
	def getMaleRatio(self):
		return self.getNumGender(0) / self.getNumGender(1) #0 = "male"
		
	#etc.
	
	def addOccupant(self, individual):
		#self.occupants ...
		pass
	
	def removeOccupant(self, individualID):
		#if individualID in IDs of set of people
		pass
