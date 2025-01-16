import random

class Person():
    def __init__(self, name):
        self.name = name
        self.infected = False
        self.infected_days = 0
        self.home = None
        self.past_infected = False
        self.Count = False
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
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].home = i
    return Households

def InfectHuman(Households):
    Households[random.randint(0, len(Households))][random.randint(0, 2)].infected = True

def DisplayInfo(Households):
    for i in range(len(Households)):
        print(f"Household {i+1}:")
        for j in range(len(Households[i])):
            print(f"\t{Households[i][j].home} and {Households[i][j].infected}")

def Morning(Households):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Morning = random.randint(0, 25)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Morning)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Morning in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                Households[i][j].infected = True
                Households[i][j].infected_days = 0
    
def Midday(Households):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Midday = random.randint(0, 25)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Midday)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Midday in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                Households[i][j].infected = True
                Households[i][j].infected_days = 0

def Evening(Households):
    warningareas = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Evening = random.randint(0, 25)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                warningareas.append(Households[i][j].Evening)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Evening in warningareas and not Households[i][j].infected and not Households[i][j].past_infected:
                Households[i][j].infected = True
                Households[i][j].infected_days = 0

def Home(Households):
    House_exposed = False
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].infected:
                House_exposed = True
        if House_exposed:
            for j in range(len(Households[i])):
                if not Households[i][j].infected and not Households[i][j].past_infected:
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
    Total_days = int(input("Enter the number of days: "))
    Households = CreatePopulation(Population)
    InfectHuman(Households)
    #DisplayInfo(Households)
    total_infected = sum(1 for i in range(len(Households)) for j in range(len(Households[i])) if Households[i][j].infected)
    current_infected = total_infected

    for i in range(Total_days):
        DayCycle(Households)
        day += 1
        current_infected = sum(1 for i in range(len(Households)) for j in range(len(Households[i])) if Households[i][j].infected)
        total_infected += current_infected
        if day == 7:
            week += 1
            print(f"Week {week}: {current_infected} currently infected")
    
    print(f"Sim Over\nTotal Infected: {total_infected}")
    print(f"Percentage Infected: {total_infected/Population*100}%")

main()