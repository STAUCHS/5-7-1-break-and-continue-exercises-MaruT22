#-------------------------------------------------------------------------
# Name:Question2
# Purpose:Create a loop that will add the numbers from 5 to 20, inclusive, but not any multiples of 3. (HINT: Use modulus)

# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
number = 5
sum = 0
while number != 20:
    
    if number % 3 != 0: 
        sum = sum + number
    else:
        continue
    number = number + 1
    print(sum)
