#-------------------------------------------------------------------------
# Name:BankPIN.
# Purpose:The bank ATMs require the user to enter their PIN and to validate their PIN so they can access their account. Create a program that checks the user has entered the correct 4-digit PIN. Make sure to store their correct PIN in a variable.  

# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

print ("WELCOME TO STA BANK!")
pin = 1234
while True:
    enter = int(input("enter pin: "))
    if pin == enter:
        break
    else:
        print("Incorrect PIN. Try again.")
print ("PIN accepted. You may now access your account.")