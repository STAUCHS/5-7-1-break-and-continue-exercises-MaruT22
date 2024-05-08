#-------------------------------------------------------------------------
# Name: loop 
# Purpose: a loop that prints numbers from 0 to 10, inclusive, but skip the number 7.
# Author:     Teng.M
# Created:    6/5/2024
#-------------------------------------------------------------------------
guess = 0

while guess != 11:
    if guess != 7:
        print (guess)
        guess = guess + 1
    else:
        guess += 1 