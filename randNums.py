import random

#sum of dice rolled, not sure if this is the best way to keep track of the rolls
#also isnt working right 
rollSum = 0

#dice functions
def d20():
    global rollSum
    roll = random.randint(1, 20)
    print("d20 > ",roll)
    rollSum += roll
    #print(rollSum) #test print

def d12():
    global rollSum
    roll = random.randint(1, 12)
    print("d12 > ",roll)
    rollSum += roll

def d10():
    global rollSum
    roll = random.randint(1, 10)
    print("d10 > ",roll)
    rollSum += roll

def d8():
    global rollSum
    roll = random.randint(1, 8)
    print("d8 > ",roll)
    rollSum += roll

def d6():
    global rollSum
    roll = random.randint(1, 6)
    print("d6 > ",roll)
    rollSum += roll

def d4():
    global rollSum
    roll = random.randint(1, 4)
    print("d4 > ",roll)
    rollSum += roll

def d100():
    global rollSum
    roll = random.randint(1, 100)
    print("d100 > ",roll)
    rollSum=rollSum+roll

#function for rolling multiple dice
def rollDice(d20Amt, d12Amt, d10Amt, d8Amt, d6Amt, d4Amt, d100Amt):
    global rollSum 
    rollsum = 0 #resets roll
    print("---roll---")
    for x in range(d20Amt):
        d20()
    for x in range(d12Amt):
        d12()
    for x in range(d10Amt):
        d10()
    for x in range(d8Amt):
        d8()
    for x in range(d6Amt):
        d6()
    for x in range(d4Amt):
        d4()
    for x in range(d100Amt):
        d10()
    print("Roll sum > ", rollSum)

#amount of dice rolled
d20Amt = 1
d12Amt = 1
d10Amt = 1
d8Amt = 1
d6Amt = 1
d4Amt = 1
d100Amt = 1

#call function
rollDice(d20Amt, d12Amt, d10Amt, d8Amt, d6Amt, d4Amt, d100Amt)

#dice test
# print("d20 - ")
# d20()
# print("d12 - ")
# d12()
# print("d10 - ")
# d10()
# print("d8 - ")
# d8()
# print("d6 - ")
# d6()
# print("d4 - ")
# d4()
# print("d100 - ")
# d100()
