from occupant import Occupant

people = []

for i in range(1, 1000):
    people.append(Occupant(
        name = 'Nome',
        surname = 'Cognome',
        birth = '01/01/1980',
        gender = False,
        nationality = 'Ucranian',
        religion = 'Christian',
        relatives = [],
        triage = 0
    ))

for i, person in enumerate(people):
    print(i, person)