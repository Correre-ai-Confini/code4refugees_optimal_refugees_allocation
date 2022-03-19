from occupant import Occupant
from faker import Faker
from random import choice

class _Faker(Faker):
    def religion(self):
        return choice(['Christian', 'Muslim', 'Orthodox'])
    def nationality(self):
        # TODO Add more nationalities
        return choice(['Ucranian', 'Belarus', 'Russian', 'Romanian', 'Italian', 'Chinese'])


faker = _Faker()

people = []

for i in range(1, 1000):
    people.append(Occupant(
        name = faker.name(),
        surname = faker.last_name(),
        birth = faker.past_date(),
        gender = faker.pybool(),
        nationality = faker.nationality(),
        religion = faker.religion(),
        relatives = [],
        triage = faker.pyint(0, 4)
    ))

for i, person in enumerate(people):
    print(i, person)