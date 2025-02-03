import random

class Person:
    def __init__(self, name):
        self.name = name
        self.infected = False
        self.infected_days = 0
        self.home = None
        self.past_infected = False
        self.Count = False
        self.Morning = None
        self.Midday = None
        self.Evening = None
        self.Exposed = False

def CreatePopulation(people):
    houses = (people // 3) + (people % 3)
    humans = []
    Households = []
    for i in range(people):
        humans.append(Person(f"Person {i + 1}"))
    for i in range(houses):
        home = []
        for j in range(3):
            if humans:
                home.append(humans.pop(0))
        Households.append(home)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].home = i + 1

    return Households

def Infect(Households):
    house_i = random.randint(0, len(Households) - 1)
    person_i = random.randint(0, len(Households[house_i]) - 1)
    Households[house_i][person_i].infected = True

def Morning(Households, locations):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Morning = random.randint(0, locations)
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Morning)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Morning in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                Households[i][j].Exposed = True

def Midday(Households, locations):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Midday = random.randint(0, locations)
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Midday)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Midday in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                Households[i][j].Exposed = True

def Evening(Households, locations):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Evening = random.randint(0, locations)
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Evening)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Evening in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                Households[i][j].Exposed = True

def Home(Households):
    for i in range(len(Households)):
        HomeExposed = False
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                HomeExposed = True
        if HomeExposed:
            for j in range(len(Households[i])):
                if not Households[i][j].infected and not Households[i][j].past_infected:
                    Households[i][j].Exposed = True

def DayCycle(Households, locations, infectionRate):
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                Households[i][j].infected_days += 1
                if Households[i][j].infected_days == 3:
                    Households[i][j].infected = False
                    Households[i][j].infected_days = 0
                    Households[i][j].past_infected = True
            elif Households[i][j].Exposed and not Households[i][j].past_infected and not Households[i][j].infected:
                number = random.randint(1, infectionRate)
                if number == 1:
                    Households[i][j].infected = True
                    Households[i][j].infected_days = 0
            Households[i][j].Exposed = False
    
    Morning(Households, locations)
    Midday(Households, locations)
    Evening(Households, locations)
    Home(Households)

def Main():
    day = 0
    people = int(input("Enter the number of people: "))
    locations = int(input("Enter the number of locations: "))
    infectionRate = int(input("Enter the infection rate: "))
    days = int(input("Enter the number of days: "))
    if people <= 0 or locations <= 0 or infectionRate <= 0 or days <= 0:
        print("Invalid input. Exiting")
        return
    Households = CreatePopulation(people)
    Infect(Households)

    total_infected = sum(1 for household in Households for person in household if person.infected or person.past_infected)

    while day <= days:
        DayCycle(Households, locations, infectionRate)
        current_infected = sum(1 for household in Households for person in household if person.infected)
        
        print(f"Day {day}: {current_infected} currently infected")

        if current_infected == 0:
            print(f"All infections resolved by day {day}. Ending simulation early.")
            break
            
        day += 1

    total_infected = sum(1 for household in Households for person in household if person.infected or person.past_infected)
    print(f"Simulation Over\nTotal Infected: {total_infected}")
    print(f"Percentage Infected: {total_infected / people * 100:.2f}%")
        
Main()