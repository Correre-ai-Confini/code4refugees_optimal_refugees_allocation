class Tent:
	def __init__(self, **kwargs):
		self.id = kwargs['id'] #string
		self.maxSpace = kwargs['maxSpace'] #integer
		self.occupants = kwargs['occupants'] #array(Occupant)
		self.medicalSupport = kwargs['MedicalSupport'] #integer with same scale as occupant.triage.
		
	def __str__(self):
		return ("Tent ID: " + str(self.id) + "\n" + "Tent Max Space: " + str(self.maxSpace) + "\n" + "Tent Occupants: " + str(self.occupants)  + "\n" + "Tent Level of Medical Support: " + str(self.medicalSupport))

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
	
	def getOccupantByID(self, id):
        	return next((individual for individual in self.occupants if individual.id == id), None)
	
	def addOccupant(self, individual):
		self.occupants.append(individual)
	
	def removeOccupant(self, individual):
		if individual in self.occupants : self.occupants.remove(individual)
