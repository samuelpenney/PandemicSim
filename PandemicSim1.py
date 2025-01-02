import random
'''
Locations:
    0 - Home
    1 - Coffee Shop
    2 - Gym
    3 - Office Building 1
    4 - Office Building 2
    5 - Office Building 3
    6 - Restaurant
    7 - Grocery Store
    8 - Park

Transit Types:
    1 - Walking
    2 - Car
    3 - Public Transport
    4 - Taxi
    5 - Biking
'''
class Person:
    #infected = False
    def __init__(self, name):
        self.name = name
        self.infected = False
        self.infected_days = 0
    Morning = None
    Midday = None
    Evening = None
    Transit = None

class NTFR(Person):
    Morning = 1
    Midday = 3
    Evening = 0
    Transit = 2
class NTFV2(Person):
    Morning = 2
    Midday = 3
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    else:
        Evening = 0
    Transit = 2
class NTFV3(Person):
    Morning = 0
    Midday = 3
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    elif number == 3:
        Evening = 8
    elif number == 4:
        Evening = 2
    else:
        Evening = 0
class NTFV4(Person):
    Morning = 0
    Midday = 3
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    else:
        Evening = 0
class NTF2(Person):
    Morning = 1
    Midday = 4
    Evening = 0
    Transit = 2
class NTF2V2(Person):
    Morning = 2
    Midday = 4
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    else:
        Evening = 0
    Transit = 2
class NTF2V3(Person):
    Morning = 0
    Midday = 4
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    elif number == 3:
        Evening = 8
    elif number == 4:
        Evening = 2
    else:
        Evening = 0
class NTF2V4(Person):
    Morning = 0
    Midday = 4
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    else:
        Evening = 0
class NTF3(Person):
    Morning = 1
    Midday = 5
    Evening = 0
    Transit = 2
class NTF3V2(Person):
    Morning = 2
    Midday = 5
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    else:
        Evening = 0
    Transit = 2
class NTF3V3(Person):
    Morning = 0
    Midday = 5
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    elif number == 3:
        Evening = 8
    elif number == 4:
        Evening = 2
    else:
        Evening = 0
class NTF3V4(Person):
    Morning = 0
    Midday = 5
    number = random.randint(1, 7)
    if number == 1:
        Evening = 6
    elif number == 2:
        Evening = 7
    else:
        Evening = 0
def CreatePopulation(people):
    humans = []
    for i in range(people):
        number = random.randint(1, 12)
        if number == 1:
            human = NTFR(f"Bot {i} - NTFR")
        elif number == 2:
            human = NTFV2(f"Bot {i} - NTFV2")
        elif number == 3:
            human = NTFV3(f"Bot {i} - NTFV3")
        elif number == 4:
            human = NTFV4(f"Bot {i} - NTFV4")
        elif number == 5:
            human = NTF2(f"Bot {i} - NTF2")
        elif number == 6:
            human = NTF2V2(f"Bot {i} - NTF2V2")
        elif number == 7:
            human = NTF2V3(f"Bot {i} - NTF2V3")
        elif number == 8:
            human = NTF2V4(f"Bot {i} - NTF2V4")
        elif number == 9:
            human = NTF3(f"Bot {i} - NTF3")
        elif number == 10:
            human = NTF3V2(f"Bot {i} - NTF3V2")
        elif number == 11:
            human = NTF3V3(f"Bot {i} - NTF3V3")
        else:
            human = NTF3V4(f"Bot {i} - NTFV2")
        humans.append(human)
    return humans

def infect(humans):
    human = random.choice(humans)
    human.infected = True

def Morning(humans, infectRate):
    warningAreas = []
    for human in humans:
        if human.infected:
            warningAreas.append(human.Morning)
    for human in humans:
        if human.Morning in warningAreas and human.infected == False:
            number = random.randint(1, infectRate)
            if number == 1:
                human.infected = True
                human.infected_days = 0

def Midday(humans, infectRate):
    warningAreas = []
    for human in humans:
        if human.infected:
            warningAreas.append(human.Midday)
    for human in humans:
        if human.Midday in warningAreas and human.infected == False:
            number = random.randint(1, infectRate)
            if number == 1:
                human.infected = True
                human.infected_days = 0

def Evening(humans, infectRate):
    warningAreas = []
    for human in humans:
        if human.infected:
            warningAreas.append(human.Evening)
    for human in humans:
        if human.Evening in warningAreas and human.infected == False:
            number = random.randint(1, infectRate)
            if number == 1:
                human.infected = True
                human.infected_days = 0
            
def Transit(humans, infectRate):
    for human in humans:
        if human.Transit == 3 and human.infected:
            exposed = True
    for human in humans:
        if human.Transit == 3 and not human.infected and exposed == True:
            number = random.randint(1, infectRate)
            if number == 1:
                human.infected = True
                human.infected_days = 0

def DayCycle(humans, infectRate, MortalityRate):
    passed_humans = []
    for human in humans:
        if human.infected:
            human.infected_days += 1
            if human.infected_days == 14:
                if random.randint(1, MortalityRate) == 1:
                    passed_humans.append(human)
                else:
                    human.infected = False
                    human.infected_days = 0

    Morning(humans, infectRate)
    Midday(humans, infectRate)
    Evening(humans, infectRate)
    Transit(humans, infectRate)

    for human in passed_humans:
        humans.remove(human)
    return len(passed_humans)

def Main():
    days = 0
    week = 0
    people = int(input("Enter the number of people: "))
    humans = CreatePopulation(people)
    infect(humans)
    infectRate = int(input("Enter the infection rate: "))
    TotalDays = int(input("Enter the number of days to simulate: "))
    MortalityRate = int(input("Enter the mortality rate: "))
    total_infected = sum(1 for human in humans if human.infected)
    current_infected = total_infected
    Total_Dead = 0
    
    for i in range(TotalDays):
        dead = DayCycle(humans, infectRate, MortalityRate)
        days += 1
        current_infected = sum(1 for human in humans if human.infected)
        total_infected += sum(1 for human in humans if human.infected and human.infected_days == 1)
        Total_Dead += dead
        if days % 7 == 0:
            week += 1
            print(f"Week {week}: {current_infected} currently infected")

    print(f"Sim Over\nTotal Infected: {total_infected}")
    print(f"Percentage Infected: {total_infected/people*100}%")
    print(f"Total Dead: {Total_Dead}")

Main()
