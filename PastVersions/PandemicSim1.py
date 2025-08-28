import random
import Testing.TestingClasses as tc
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
    humans = tc.CreatePopulation(people)
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
