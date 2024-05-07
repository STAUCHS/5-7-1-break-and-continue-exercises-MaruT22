#-------------------------------------------------------------------------
# Name:Question3
# Purpose:Ask the user for a starting number and an ending number. The program will get the sum of all the numbers from the start to the end (using a loop). However, our program is a bit of a diva: the program will stop summing the numbers if it encounters a 13 or a 31. It will still output the sum up to that point.

# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

start = int(input("start number: "))
end= int(input("end number: "))
sum = 0
while start != end:
    if start == 13:
        print(start)
        break
    elif start == 31:
        print(start)
        break
    else:
        sum = sum + start
        start += 1 

print (sum)