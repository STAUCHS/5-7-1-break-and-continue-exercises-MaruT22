#-------------------------------------------------------------------------
# Name:DiceDoubles
# Purpose:a program that simulates dice rolls until the dice show doubles (the same number on both dice).
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
import random

while True:
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    if d1 == d2:
        print (f"Roll #1:{d1}")
        print (f"Roll #2:{d2}")
        print(f"The total is {d1+d2}!")
        break
    else:
        print (f"Roll #1:{d1}")
        print (f"Roll #2:{d2}")
        print(f"The total is {d1+d2}!")
