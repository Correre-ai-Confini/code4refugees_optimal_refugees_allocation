class scoreFunction:
  def __init__(self, listOfTents, batchRefugeesMoving, refugeesAllocationVector):
    self.scoreMatrixMedical = [ [ min( 0, tent.medSupport - refugee.triage ) for tent in listOfTents ] for refugeeTriage in batchRefugeesMoving ]
  
  
  #Medical support score
  
	#Compact form
	#refugeesAllocationVector is the (test) solution. refugeesAllocationVector[i] shows the ID of tent where refugee would be placed
	def computeMedScore(refugeesAllocationVector) :
	  score=0
		for i in range(len(refugeesAllocationVector)) :
      score+= scoreMatrixMedical[i][refugeesAllocationVector[i]-1]
    return score
		
	#Matrix form

#Example:


#-----------------------------------------
	#Families

	#families is a matrix. families[i] describes the i-th family. If element j of batchRefugeesMoving is part of family i, then families[i][j] == 1, and 0 otherwise.
	#families = generateFamilyMatrix(batchRefugeesMoving)
  
  def computeFamilyScore(refugeesAllocationVector) :
	  #MP_fam = ...
	  #famAllocations = X * MP_fam
	  family_size = [ sum(family) for family in families]

	  famAllocations_perc = [ [ numOfMembersInTent / family_size[i] for numOfMembersInTent in famAllocations[i] ] for i in range(len(famAllocations)) ]

	  famAllocations_perc_mod = famAllocations_perc
	  for row in famAllocations_perc_mod :
	  	for element in row :
		  	if element==0 : element=1 #forall famAllocations_perc[i][j] : if famAllocations_perc[i][j]==0 : famAllocations_perc_mod[i][j]=1
			
	  scoreVectorFamily = [ min(row) for row in famAllocations_perc_mod ]
	  return sum(scoreVectorFamily)

	#Example:
	#famAllocations =
	#1 2 0  --> of family 0, 1 member is in tent 0, 2 members are in tent 1, no one in tent 2.
	#0 0 1  --> family 1 has only one member in tent 2
	#2 0 0  --> family 2 has 2 members in tent 0
	#
	#family_size = [3, 1, 2]
	#
	#famAllocations_perc_mod =
	#0.33 0.66  1
	# 1    1    1
	# 1    1    1
	#
	#scoreVectorFamily = [0.33, 1, 1] #Most "lonely" fraction of family yields score.
