import random

#function for rolling a die with "faces" sides
def die(faces):
    roll = random.randint(1, faces)
    print("d",faces," roll > ",roll)
    return roll

##takes in user input to roll a die with any amount of sides
#sides = int(input("Enter sides > "))
#die(sides)

#funtion for rolling multiple dice
def dice(d20amt, d12amt, d10amt, d8amt, d6amt, d4amt, d100amt):
    rollTotal = 0
    for x in range(d20amt):
        rollTotal += die(20)
    for x in range(d12amt):
        rollTotal += die(12)
    for x in range(d10amt):
        rollTotal += die(10)
    for x in range(d8amt):
        rollTotal += die(8)
    for x in range(d6amt):
        rollTotal += die(6)
    for x in range(d4amt):
        rollTotal += die(4)
    for x in range(d100amt):
        rollTotal += die(100)

    print(rollTotal)

##rolls one of each die, test
#dice(1, 1, 1, 1, 1, 1, 1)

#takes user input for amount of dice rolled
xd20 = int(input("Number of d20s > "))
xd12 = int(input("Number of d12s > "))
xd10 = int(input("Number of d10s > "))
xd8 = int(input("Number of d8s > "))
xd6 = int(input("Number of d6s > "))
xd4 = int(input("Number of d4s > "))
xd100 = int(input("Number of d100s > "))
#rolls dice based off user input
dice(xd20, xd12, xd10, xd8, xd6, xd4, xd100)
