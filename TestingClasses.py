import random
class Person():
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
            humans.append(NTFR("NTFR"))
        elif number == 2:
            humans.append(NTFV2("NTFV2"))
        elif number == 3:
            humans.append(NTFV3("NTFV3"))
        elif number == 4:
            humans.append(NTFV4("NTFV4"))
        elif number == 5:
            humans.append(NTF2("NTF2"))
        elif number == 6:
            humans.append(NTF2V2("NTF2V2"))
        elif number == 7:
            humans.append(NTF2V3("NTF2V3"))
        elif number == 8:
            humans.append(NTF2V4("NTF2V4"))
        elif number == 9:
            humans.append(NTF3("NTF3"))
        elif number == 10:
            humans.append(NTF3V2("NTF3V2"))
        elif number == 11:
            humans.append(NTF3V3("NTF3V3"))
        else:
            humans.append(NTF3V4("NTF3V4"))
    return humans