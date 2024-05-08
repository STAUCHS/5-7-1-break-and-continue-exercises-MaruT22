#-------------------------------------------------------------------------
# Name:Question4

# Purpose:Create an infinite loop using while True:. In that loop ask the user for a word. For each word they enter, output the following "Your word: {word}". If ever they enter the word "stop", the program will break out of the loop. Finally the program will output "Goodbye!".

# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

while True:
    inputed = input("Enter a word: ")
    if inputed == "stop":
        break
    else:
        print (f"Your word: {inputed}")

print ("Goodbye!")