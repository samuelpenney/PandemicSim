# Final Version of the Pandemic Simulation
import random # Imports the random module for number generation
import matplotlib.pyplot as plt # Imports the matplotlib module for plotting
import matplotlib.animation as animation # Imports the animation module from matplotlib for creating animations
import time # Imports the time module for tracking elasped time

class Person: # Represents an individual in the simulation
    def __init__(self, name): # Initializes a Person object with a name and default attributes
        self.name = name # Name of the person
        self.infected = False # Infection status
        self.infected_days = 0 # Number of days the person has been infected 
        self.home = None # Home identifier
        self.past_infected = False # Past infection status
        self.Morning = None # Morning location
        self.Midday = None # Midday location
        self.Evening = None # Evening location
        self.Exposed = False # Exposure status

def CreatePopulation(people): # Creates a population of people and organizes them into households
    houses = (people // 3) + (people % 3) # Calculate number of houses needed
    humans = [] # List to hold every person
    Households = [] # List to hold households
    for i in range(people): # Create Person objects using people input and adds them into a list
        humans.append(Person(f"Person {i + 1}")) # Create a new person object in the list
    for i in range(houses): # Create households with up to 3 people each
        home = [] # List to hold people in a household
        for j in range(3): # Add up to 3 people to each household
            if humans: # Check if there are still people left to assign to households
                humans[0].home = i + 1 # Assign home number to the person
                home.append(humans.pop(0)) # Add the person to the household and remove them from the main list
                
        Households.append(home) # Add the household to the list of households

    house_i = random.randint(0, len(Households) - 1) # Randomly select a household to infect one person
    person_i = random.randint(0, len(Households[house_i]) - 1) # Randomly select a person withing that household
    Households[house_i][person_i].infected = True # Infect that person
    return Households # Return the list of households

def DayEvent(Households, locations): # Simulates daily events where people will visit different locations and potentially spread the infection
    MorningWarning = [] # Lists to track locations visited by infected individuals
    MiddayWarning = [] 
    EveningWarning = []
    for i in range(len(Households)): # Iterate through each household
        for j in range(len(Households[i])): # Iterate through each person in the household
            Households[i][j].Morning = random.randint(0, locations) # Assign random locations for morning, midday, and evening
            Households[i][j].Midday = random.randint(0, locations)
            Households[i][j].Evening = random.randint(0, locations)
            if Households[i][j].infected: # If the person is infected, add their locations to the warning lists
                MorningWarning.append(Households[i][j].Morning) 
                MiddayWarning.append(Households[i][j].Midday)
                EveningWarning.append(Households[i][j].Evening)
    for i in range(len(Households)): # Iterate through each household again to check for exposure
        for j in range(len(Households[i])): # Iterate through each person in the household
            if Households[i][j].Morning in MorningWarning or Households[i][j].Midday in MiddayWarning or Households[i][j].Evening in EveningWarning and not Households[i][j].infected and not Households[i][j].past_infected: # If the person's locations match any in the warning lists and they are not already infected or previously infected
                Households[i][j].Exposed = True # Mark the person as exposed

def Home(Households): # Simulates the spread of infection within households
    for i in range(len(Households)): # Iterate through each household
        HomeExposed = False # Flag to track if any member of the household is exposed
        for j in range(len(Households[i])): # Iterate through each person in the household
            if Households[i][j].Exposed: # If any person in the household is exposed
                HomeExposed = True 
                break
        if HomeExposed: # If the household is exposed, mark all uninfected and never-infected members as exposed
            for j in range(len(Households[i])): # Iterate through each person in the household again
                if not Households[i][j].infected and not Households[i][j].past_infected: # If the person is not infected and has never been infected
                    Households[i][j].Exposed = True 

def DayCycle(Households, locations, infectionRate): # Simulates a full day cycle including infection spread and daily events
    for i in range(len(Households)): # Iterate through each household
        for j in range(len(Households[i])): # Iterate through each person in the household
            number = random.randint(1, infectionRate) # Generate a random number to determine if exposure leads to infection
            if Households[i][j].infected and Households[i][j].infected_days < 3: # If the person is infected and has been infected for less than 3 days
                Households[i][j].infected_days += 1 # Increment the number of days they have been infected
            elif Households[i][j].infected and Households[i][j].infected_days >= 3: # If the person has been infected for 3 or more days
                Households[i][j].infected = False # They recover and are no longer infected
                Households[i][j].past_infected = True # Mark them as having been infected in the past, and past peoeple cannot be reinfected
            elif Households[i][j].Exposed and not Households[i][j].past_infected and not Households[i][j].infected and number == 1: # If the person is exposed, has never been infected, is not currently infected, and the random number indicates infection
                Households[i][j].infected = True # Infect the person
            Households[i][j].Exposed = False # Reset exposure status for the next day
    
    DayEvent(Households, locations) # Simulate daily events
    Home(Households) # Simulate household infection spread

def Main(): # Main function to run the simulation
    people = int(input("Enter the number of people: ")) # Get users input for simulation
    locations = int(input("Enter the number of locations: ")) # 
    infectionRate = int(input("Enter the infection rate: "))
    days = int(input("Enter the number of days: "))
    start_time = time.time() # Start the timer to track elasped time
    if people <= 0 or locations <= 0 or infectionRate <= 0 or days <= 0: # Validate user input
        print("Invalid input. Please enter positive integers.")
        return
    Households = CreatePopulation(people) # Create the population

    never_infected = [] # Lists to track the number of never infected, currently infected, and past infected individuals over time
    currently_infected = [] 
    past_infected = []
    days_list = []

    fig, ax = plt.subplots() # Set up the plot for animation

    def update(day): # Update function for each day in the animation
        DayCycle(Households, locations, infectionRate) # Simulate a day cycle
        current_infected = sum(1 for household in Households for person in household if person.infected) # Count current infections
        past_infected_count = sum(1 for household in Households for person in household if person.past_infected) # Count past infections
        never_infected_count = people - current_infected - past_infected_count # Calculate never infected individuals

        never_infected.append(never_infected_count) # Append counts to respective lists
        currently_infected.append(current_infected) 
        past_infected.append(past_infected_count)
        days_list.append(day)

        ax.clear() # Clear the previous plot
        ax.stackplot(days_list, currently_infected, past_infected, never_infected, colors=['red', 'gray', 'blue'], labels=['Currently Infected', 'Past Infected', 'Never Infected']) # Create a stacked area plot
        ax.set_xlabel('Day') # Set plot labels and title
        ax.set_ylabel('Population') 
        ax.set_title('Epidemic Simulation')
        ax.legend(loc='upper left')


        print(f"Day {day}: {current_infected} currently infected") # Print the current day and number of infections

        if current_infected == 0: # If there are no current infections, end the simulation early
            stop_time = time.time() # Stop the timer
            elasped_time = stop_time - start_time # Calculate elasped time
            print(f"All infections resolved by day {day}. Ending simulation early.") # Sends message to command line
            total_infected = sum(1 for household in Households for person in household if person.infected or person.past_infected) # Calculate total number of people who were infected at any point
            print(f"Simulation Over\nTotal Infected: {total_infected}") # Show total infected
            print(f"Percentage Infected: {total_infected / people * 100:.2f}%") # Show percentage of population that was infected
            print(f"Elapsed Time: {elasped_time:.2f} seconds") # Show elasped time
            ani.event_source.stop() # Stop the animation
            return False
             
        return True

    ani = animation.FuncAnimation(fig, update, frames=range(days), repeat=False) # Create the animation
    plt.show() # Display the plot

if __name__ == "__main__": # Run the main function if the script is executed directly
    Main()

    