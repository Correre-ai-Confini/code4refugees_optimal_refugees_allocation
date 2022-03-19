from occupant import Occupant
from faker import Faker

faker = Faker()

people = []

for i in range(1, 1000):
    people.append(Occupant(
        name = faker.name(),
        surname = faker.last_name(),
        birth = faker.past_date(),
        gender = faker.pybool(),
        nationality = faker.country(),
        religion = faker.country(),
        relatives = [],
        triage = faker.pyint(0, 4)
    ))

for i, person in enumerate(people):
    print(i, person)