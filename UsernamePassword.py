#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
username = "Maru"
password = "1232"
while True:
    password_input = (input("Enter your username: "))
    username_input = (input("Enter your password: "))
    if password ==  password_input and username == username_input:
        break
    elif password != password_input and username != username_input: 
        print("Username and password incorrect.")
    elif password != password_input and username == username_input: 
        print("Password incorrect.")
    elif password == password_input and username != username_input: 
        print("Username incorrect.")
print ("Welcome!")