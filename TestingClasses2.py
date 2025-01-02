import TestingClasses as tc
people = 100


humans = tc.CreatePopulation(people)
for human in humans:
    print(human.name, end=" ")
