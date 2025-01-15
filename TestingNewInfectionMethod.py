import random
Population = int(input("Enter the population: "))
Houses = (Population // 3) + (Population % 3)

'''
people = []
Households = []
for i in range(Population):
    people.append(f"Person{i + 1}")

for i in range(Houses):
    home = []
    for j in range(3):
        if people:
            human = people.pop(0)
            home.append(human)
    Households.append(home)
'''
class Person():
    def __init__(self, name):
        self.name = name
        self.infected = False
        self.infected_days = 0
    Morning = None
    Midday = None
    Evening = None


def CreatePopulation(people):
    houses = (people // 3) + (people % 3)
    humans = []
    Households= []
    for i in range(people):
        humans.append(Person(f"Person{i + 1}"))
    for i in range(houses):
        home = []
        for j in range(3):
            if humans:
                home.append(humans.pop(0))
        Households.append(home)
    return Households

def InfectHuman(HouseHolds):
    number = random.randint(0, len(Households))
    number2 = random.randint(0, 2)
    Households[number][number2].infected = True



Households = CreatePopulation(Population)
InfectHuman(Households)

for i in range(len(Households)):
    print(f"Household {i + 1}:")
    for j in range(len(Households[i])):
        print(f"\t{Households[i][j].infected}")