class Occupant:
    def __init__(self, **kwargs):
        self.name = kwargs['name'] #string
        self.surname = kwargs['surname'] #string
        self.birth = kwargs['birth'] #string
        self.gender = kwargs['gender'] #bool false-> male, true-> female
        self.nationality = kwargs['nationality'] #string
        self.religion = kwargs['religion'] # string
        self.relative = kwargs['relatives'] #array(Occupant)
        self.triage = kwargs['triage'] #int: [0,4]

    def __str__(self):
        if self.gender == False:
            g= "male"
        else:
            g = "female"
        if self.relative == None: return (self.name+" "+self.surname+", born: "+self.birth+", nationality: "+self.nationality+", religion: "+ self.religion+". \n \
        Triage code:" +str(self.triage))
        else:
            r = [i.name+" "+i.surname for i in self.relative]
        
            return (self.name+" "+self.surname+", born: "+self.birth+", nationality: "+self.nationality+", religion: "+ self.religion+". \n \
        Relatives:"+ str(r)[1:-2]+"\n Triage code:" +str(self.triage))  
