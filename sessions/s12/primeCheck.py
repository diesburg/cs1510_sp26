"""
File : primeCheck.py
Author : Diesburg
Description : Is the input prime?
"""

# Let's get the number to check and do error checking
number = int(input("Please enter a number greater than 2. "))
while number<2:
    number = int(input("Please enter a number greater than 2. "))

isPrime = True #break out condition

# Can we implement the while loop as a for loop?

divisor = 2

while divisor<number and isPrime:
    if number%divisor==0:
        print("The number",number,"is divisible by",\
              divisor)
        isPrime=False   # Going to break out
    divisor=divisor+1

# And the verdict is...
if isPrime:
    print("That number is prime")
else:
    print("That number is NOT prime")
