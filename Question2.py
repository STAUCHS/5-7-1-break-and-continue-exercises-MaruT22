#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
number = 5
sum = 0
while number != 20:
    
    if number % 3 == 0: 
        sum = sum + number
    else:
        continue
    number = number + 1
    print(sum)
