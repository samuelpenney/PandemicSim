import java.util.*; // Import necessary libraries

class Human{ // Class to represent each individual in the simulation
    String name; // Name of the individual
    boolean infected = false; // Current infection status
    boolean pastInfected = false; // Past infection status
    boolean exposed = false; // Exposure status
    int infectedDays = 0; // NUmber of days infected
    int home; // Home Number
    int morning, midday, evening; // Locations visited during the day


    public Human(String name) { 
        this.name = name; // Constructor to initialize the name
    }
}


public class EpidemicSim { // Main class for the epidemic simulation


    public static Random rand = new Random(); // Random number generator


    public static List<List<Human>> createPopulation(int people) { // Method to create the population and households
        int houses = (people / 3) + (people % 3); // Calculate number of houses needed
        List<Human> humans = new ArrayList<>(); // List to hold all individuals
        List<List<Human>> households = new ArrayList<>(); // List to hold households

        for (int i = 0; i < people; i++) { // Create individuals
            humans.add(new Human("Human " + (i + 1)));

        }

        for (int i = 0; i < houses; i++) { // Create households
            List<Human> home = new ArrayList<>();
            for (int j = 0; j < 3 && !humans.isEmpty(); j++) { // Add up to 3 individuals to each households
                Human p = humans.remove(0);
                p.home = i + 1;
                home.add(p);
            }
            households.add(home); // Add household to the list of households
        } 

        int houseIndex = rand.nextInt(households.size()); // Randomly infect one person at the start
        int personIndex = rand.nextInt(households.get(houseIndex).size());
        households.get(houseIndex).get(personIndex).infected = true;

        return households;
    }

    public static void dayEvent(List<List<Human>> households, int locations) { // Method to simulate daily events and infection
        List<Integer> morningWarning = new ArrayList<>(); // Lists to track locations with infected
        List<Integer> middayWarning = new ArrayList<>();
        List<Integer> eveningWarning = new ArrayList<>();


        for (List<Human> home : households) { // Assign random locations to each individual and track infected locations
            for (Human p : home) {
                p.morning = rand.nextInt(locations + 1); 
                p.midday = rand.nextInt(locations + 1);
                p.evening = rand.nextInt(locations + 1);
                if (p.infected) { // If infected, add their locations to the warning lists
                    morningWarning.add(p.morning);
                    middayWarning.add(p.midday);
                    eveningWarning.add(p.evening);
                }
            }
        }

        for (List<Human> home : households) { // Check for exposure based on locations visited
            for (Human p : home) {
                if (!p.infected && !p.pastInfected) { 
                    if (morningWarning.contains(p.morning) || middayWarning.contains(p.midday) || eveningWarning.contains(p.evening) && !p.infected && !p.pastInfected) {
                        p.exposed = true; // Mark as exposed if they visited an infected location
                    }
                }  
            }
        }


    }

    public static void homeSpread(List<List<Human>> households) { // Method to handle spread within households
        for (List<Human> home : households) {
            boolean homeExposed = home.stream().anyMatch(p -> p.infected); // Check if any member of the household is infected
            if (homeExposed) {
                for (Human p : home) {
                    if (!p.infected && !p.pastInfected) {
                        p.exposed = true; // Mark all non-infected, non-past-infected members as exposed
                    }
                }
            }
        }
    }

    public static void dayCycle(List<List<Human>> households, int locations, int infectionRate) { // Method to simulate a full day cycle
        for (List<Human> home : households) { 
            for (Human p : home) {
                int number = rand.nextInt(infectionRate) + 1; // Random number to determine infection based on infection rate
                if (p.infected && p.infectedDays < 3) {
                    p.infectedDays++; // Increment days infected if infected
                } else if (p.infected && p.infectedDays >= 3) {
                    p.infected = false; // Recover after 3 days if infected
                    p.pastInfected = true; // Mark as past infected so they can't be reinfected
                } else if (p.exposed && !p.pastInfected && !p.infected && number == 1) {
                    p.infected = true; // Infect if exposed and random chance hits
                }
                p.exposed = false; // reset exposure for the next day
            }

        }
        dayEvent(households, locations); // Calls the day event to simulate daily activities and potential exposures
        homeSpread(households); // Calls the home spread to simulate infections within households
    }


    public static void main(String[] args) { // Main method to run the simulation
        Scanner sc = new Scanner(System.in); // Scanner for user input if using user input
        /*
         * If using command line arguments is preferred
         * int people = args[0];
         * int locations = args[1];
         * int infectionRate = args[2];
         * int days = args[3];
         */
        System.out.print("Enter the number of people in the population: "); // Get user inputs for people, locations, infection rate, and days
        int people = sc.nextInt();
        System.out.print("Enter the number of locations: ");
        int locations = sc.nextInt();
        System.out.print("Enter the infection rate (1 in X chance of infection upon exposure): ");
        int infectionRate = sc.nextInt();
        System.out.print("Enter the number of days to simulate: ");
        int days = sc.nextInt();

        if (people < 1 || locations < 1 || infectionRate < 1 || days < 1) {
            System.out.println("All inputs must be positive integers greater than zero.");
            return; // Exit if inputs are invalid
        }

        long startTime = System.currentTimeMillis(); // Start time for elapsed time
        List<List<Human>> households = createPopulation(people); // Create the population

        for (int day = 0; day < days; day++) {
            dayCycle(households, locations, infectionRate); // Simulate each day

            int currentInfected = 0, pastInfected = 0; // Count current and past infected individuals
            for (List<Human> home : households) { 
                for (Human p : home) { 
                    if (p.infected) currentInfected++;
                    if (p.pastInfected) pastInfected++;
                }
            }
            int neverInfected = people - currentInfected - pastInfected; // Calculate never infected individuals
            System.out.println("Day " + (day + 1) + ": Currently Infected: " + currentInfected + ", Never Infected: " + neverInfected + ", Past Infected: " + pastInfected);

            if (currentInfected == 0) { // End simulation early if no current infections, prints results
                long elapsedTime = System.currentTimeMillis() - startTime; 
                System.out.printf("All infections resolved by day %d. Ending early.%n", day);
                int totalInfected = people - neverInfected;
                System.out.printf("Simulation Over%nTotal Infected: %d%n", totalInfected);
                System.out.printf("Percentage Infected: %.2f%%%n", (totalInfected * 100.0 / people));
                System.out.printf("Elapsed Time: %.2f seconds%n", elapsedTime / 1000.0);
                return;
            }
        }
        // Final results after all days simulated
        long elapsedTime = System.currentTimeMillis() - startTime;
        int totalInfected = 0;
        for (List<Human> home : households) {
            for (Human p : home) {
                if (p.pastInfected || p.infected) totalInfected++;
            }
        }

        System.out.println("Simulation Over");
        System.out.printf("Total Infected: %d%n", totalInfected);
        System.out.printf("Percentage Infected: %.2f%%%n", (totalInfected * 100.0 / people));
        System.out.printf("Elapsed Time: %.2f seconds%n", elapsedTime / 1000.0);
    }
}