import random

class Person():
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

def CreatePopulation(people):
    houses = (people // 3) + (people % 3)
    humans = []
    Households = []
    for i in range(people):
        humans.append(Person(f"Person{i + 1}"))
    for i in range(houses):
        home = []
        for j in range(3):
            if humans:
                home.append(humans.pop(0))
        Households.append(home)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].home = i


    return Households

def InfectHuman(Households):
    household_index = random.randint(0, len(Households) - 1)
    person_index = random.randint(0, len(Households[household_index]) - 1)
    Households[household_index][person_index].infected = True

def DisplayInfo(Households):
    for i in range(len(Households)):
        print(f"Household {i+1}:")
        for j in range(len(Households[i])):
            print(f"\t{Households[i][j].home} and {Households[i][j].infected}")

def Morning(Households):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Morning = random.randint(0, 100)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Morning)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Morning in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                number = random.randint(0,3)
                if number == 1:
                    Households[i][j].infected = True
                    Households[i][j].infected_days = 0
    
def Midday(Households):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Midday = random.randint(0, 100)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Midday)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Midday in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                number = random.randint(0,3)
                if number == 1:
                    Households[i][j].infected = True
                    Households[i][j].infected_days = 0

def Evening(Households):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Evening = random.randint(0, 100)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Evening)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Evening in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                number = random.randint(0,3)
                if number == 1:
                    Households[i][j].infected = True
                    Households[i][j].infected_days = 0

def Home(Households):
    for i in range(len(Households)):
        House_exposed = False
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                House_exposed = True
        if House_exposed:
            for j in range(len(Households[i])):
                if not Households[i][j].infected and not Households[i][j].past_infected:
                    number = random.randint(0,3)
                    if number == 1:
                        Households[i][j].infected = True
                        Households[i][j].infected_days = 0

def DayCycle(Households):
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                Households[i][j].infected_days += 1
                if Households[i][j].infected_days == 3:
                    Households[i][j].past_infected = True
                    Households[i][j].infected = False
                    Households[i][j].infected_days = 0
    Morning(Households)
    Midday(Households)
    Evening(Households)
    Home(Households)

def main():
    day = 0
    week = 0
    Population = int(input("Enter the number of people: "))
    if Population <= 0:
        print("Invalid population size. Exiting simulation.")
        return

    Total_days = int(input("Enter the number of days: "))
    Households = CreatePopulation(Population)
    InfectHuman(Households)

    total_infected = sum(1 for household in Households for person in household if person.infected or person.past_infected)

    for day in range(1, Total_days + 1):
        DayCycle(Households)
        current_infected = sum(1 for household in Households for person in household if person.infected)
        total_infected = sum(1 for household in Households for person in household if person.infected or person.past_infected)

        print(f"Day {day}: {current_infected} currently infected")

        if current_infected == 0:
            print(f"All infections resolved by day {day}. Ending simulation early.")
            break

        if day % 7 == 0:
            week += 1
            print(f"\tEnd of Week {week}: {current_infected} currently infected")

    if Population > 0:
        print(f"Simulation Over\nTotal Infected: {total_infected}")
        print(f"Percentage Infected: {total_infected / Population * 100:.2f}%")


main()