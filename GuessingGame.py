#-------------------------------------------------------------------------
# Name:GuessingGame
# Purpose:Add to the guessing game program we created in class by limiting the number of tries to 5.
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------


import random


num = random.randrange(1, 101)


guess = int(input("Enter a number between 1 and 100: "))
tries = 1


while guess != num and tries < 5:
  if guess > num:
    print("Guess is too high. Guess again.\n")
  else:
    print("Guess is too low. Guess again.\n")
    
  guess = int(input("Enter a guess: "))
  tries += 1


if tries < 5:
  print("Congratulations! You guessed correct!")
else:
  print(f"Sorry! Game Over! The number was {num}.")