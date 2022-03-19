from occupant import Occupant
from tent import Tent
from faker import Faker
from random import choice

# Extending Faker class to add suitable data to seeding
class _Faker(Faker):
    def religion(self):
        return choice(['Christian', 'Muslim', 'Orthodox'])
    def nationality(self):
        # TODO Add more nationalities
        return choice(['Ucranian', 'Belarus', 'Russian', 'Romanian', 'Moldovan', 'Polish', 'Italian', 'Chinese'])
        # Languages.  Romanian: {'Romanian', 'Moldovan'}. 

# Faker instance
faker = _Faker()

# Empty lists
people = []
tents = []



# People
for i in range(1, 1000):
    people.append(Occupant(
        id = faker.unique.random_int(),
        name = faker.name(),
        surname = faker.last_name(),
        birth = faker.past_date(),
        gender = faker.pybool(),
        nationality = faker.nationality(),
        religion = faker.religion(),
        relatives = [],
        triage = faker.pyint(0, 4)
    ))

# Generate relationships
for i, person in enumerate(people):
    person.relatives = [choice(people) for _ in range(4)]

for i, person in enumerate(people):
    print(i, person)


# Tents
for i in range(1, 100):
    tents.append(Tent(
        id = faker.unique.random_int(),
        maxSpace = faker.pyint(100, 200),
        occupants = faker.pyint(0, 20),
        distanceFromMed = faker.pyfloat(min_value=10, max_value=200)
    ))

for i, tent in enumerate(tents):
    #print(i, tent)
    pass
