import java.util.*;

class Human{ 
    String name; 
    boolean infected = false; 
    boolean pastInfected = false;
    boolean exposed = false; 
    int infectedDays = 0; 
    int home; 
    int morning, midday, evening;


    public Human(String name) { 
        this.name = name; 
    }
}


public class EpidemicSim { 


    public static Random rand = new Random();


    public static List<List<Human>> createPopulation(int people) { 
        int houses = (people / 3) + (people % 3); 
        List<Human> humans = new ArrayList<>(); 
        List<List<Human>> households = new ArrayList<>(); 

        for (int i = 0; i < people; i++) { 
            humans.add(new Human("Human " + (i + 1)));

        }

        for (int i = 0; i < houses; i++) { 
            List<Human> home = new ArrayList<>();
            for (int j = 0; j < 3 && !humans.isEmpty(); j++) { 
                Human p = humans.remove(0);
                p.home = i + 1;
                home.add(p);
            }
            households.add(home); 
        } 

        int houseIndex = rand.nextInt(households.size()); 
        int personIndex = rand.nextInt(households.get(houseIndex).size());
        households.get(houseIndex).get(personIndex).infected = true;

        return households;
    }

    public static void dayEvent(List<List<Human>> households, int locations) { 
        List<Integer> morningWarning = new ArrayList<>();
        List<Integer> middayWarning = new ArrayList<>();
        List<Integer> eveningWarning = new ArrayList<>();


        for (List<Human> home : households) { 
            for (Human p : home) {
                p.morning = rand.nextInt(locations + 1); 
                p.midday = rand.nextInt(locations + 1);
                p.evening = rand.nextInt(locations + 1);
                if (p.infected) { 
                    morningWarning.add(p.morning);
                    middayWarning.add(p.midday);
                    eveningWarning.add(p.evening);
                }
            }
        }

        for (List<Human> home : households) { 
            for (Human p : home) {
                if (!p.infected && !p.pastInfected) { 
                    if (morningWarning.contains(p.morning) || middayWarning.contains(p.midday) || eveningWarning.contains(p.evening) && !p.infected && !p.pastInfected) {
                        p.exposed = true; 
                    }
                }  
            }
        }


    }

    public static void homeSpread(List<List<Human>> households) { 
        for (List<Human> home : households) {
            boolean homeExposed = home.stream().anyMatch(p -> p.infected); 
            if (homeExposed) {
                for (Human p : home) {
                    if (!p.infected && !p.pastInfected) {
                        p.exposed = true; 
                    }
                }
            }
        }
    }

    public static void dayCycle(List<List<Human>> households, int locations, int infectionRate) { 
        for (List<Human> home : households) { 
            for (Human p : home) {
                int number = rand.nextInt(infectionRate) + 1; 
                if (p.infected && p.infectedDays < 3) {
                    p.infectedDays++; 
                } else if (p.infected && p.infectedDays >= 3) {
                    p.infected = false; 
                    p.pastInfected = true; 
                } else if (p.exposed && !p.pastInfected && !p.infected && number == 1) {
                    p.infected = true; 
                }
                p.exposed = false; 
            }

        }
        dayEvent(households, locations); 
        homeSpread(households); 
    }


    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
    
        System.out.print("Enter the number of people in the population: "); 
        int people = sc.nextInt();
        System.out.print("Enter the number of locations: ");
        int locations = sc.nextInt();
        System.out.print("Enter the infection rate (1 in X chance of infection upon exposure): ");
        int infectionRate = sc.nextInt();
        System.out.print("Enter the number of days to simulate: ");
        int days = sc.nextInt();

        if (people < 1 || locations < 1 || infectionRate < 1 || days < 1) {
            System.out.println("All inputs must be positive integers greater than zero.");
            sc.close();
            return;
        }

        long startTime = System.currentTimeMillis(); 
        List<List<Human>> households = createPopulation(people); 

        for (int day = 0; day < days; day++) {
            dayCycle(households, locations, infectionRate);

            int currentInfected = 0, pastInfected = 0;
            for (List<Human> home : households) { 
                for (Human p : home) { 
                    if (p.infected) currentInfected++;
                    if (p.pastInfected) pastInfected++;
                }
            }
            int neverInfected = people - currentInfected - pastInfected; 
            System.out.println("Day " + (day + 1) + ": Currently Infected: " + currentInfected + ", Never Infected: " + neverInfected + ", Past Infected: " + pastInfected);

            if (currentInfected == 0) {
                long elapsedTime = System.currentTimeMillis() - startTime; 
                System.out.printf("All infections resolved by day %d. Ending early.%n", day);
                int totalInfected = people - neverInfected;
                System.out.printf("Simulation Over%nTotal Infected: %d%n", totalInfected);
                System.out.printf("Percentage Infected: %.2f%%%n", (totalInfected * 100.0 / people));
                System.out.printf("Elapsed Time: %.2f seconds%n", elapsedTime / 1000.0);
                sc.close();
                return;
            }
        }

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
        sc.close();
    }
}