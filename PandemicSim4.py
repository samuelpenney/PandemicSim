import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

def DayEvent(Households, locations):
    MorningWarning = []
    MiddayWarning = []
    EveningWarning = []
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            Households[i][j].Morning = random.randint(0, locations)
            Households[i][j].Midday = random.randint(0, locations)
            Households[i][j].Evening = random.randint(0, locations)
            if Households[i][j].infected:
                MorningWarning.append(Households[i][j].Morning)
                MiddayWarning.append(Households[i][j].Midday)
                EveningWarning.append(Households[i][j].Evening)
    for i in range(len(Households)):
        for j in range(len(Households[i])):
            if Households[i][j].Morning in MorningWarning or Households[i][j].Midday in MiddayWarning or Households[i][j].Evening in EveningWarning and not Households[i][j].infected and not Households[i][j].past_infected:
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
    
    DayEvent(Households, locations)
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

    never_infected = []
    currently_infected = []
    past_infected = []
    days_list = []

    fig, ax = plt.subplots()
    ax.set_xlabel('Day')
    ax.set_ylabel('Population')
    ax.set_title('Infection Simulation')
    ax.legend(loc='upper left')

    def update(day):
        DayCycle(Households, locations, infectionRate)
        current_infected = sum(1 for household in Households for person in household if person.infected)
        past_infected_count = sum(1 for household in Households for person in household if person.past_infected)
        never_infected_count = people - current_infected - past_infected_count

        never_infected.append(never_infected_count)
        currently_infected.append(current_infected)
        past_infected.append(past_infected_count)
        days_list.append(day)

        ax.clear()
        ax.stackplot(days_list, currently_infected, past_infected, never_infected, colors=['red', 'gray', 'blue'], labels=['Currently Infected', 'Past Infected', 'Never Infected'])
        ax.set_xlabel('Day')
        ax.set_ylabel('Population')
        ax.set_title('Infection Simulation')
        ax.legend(loc='upper left')


        print(f"Day {day}: {current_infected} currently infected")

        if current_infected == 0:
            print(f"All infections resolved by day {day}. Ending simulation early.")
            total_infected = sum(1 for household in Households for person in household if person.infected or person.past_infected)
            print(f"Simulation Over\nTotal Infected: {total_infected}")
            print(f"Percentage Infected: {total_infected / people * 100:.2f}%")
            ani.event_source.stop()
            return False
            
        return True

    ani = animation.FuncAnimation(fig, update, frames=range(days), repeat=False)
    plt.show()

Main()