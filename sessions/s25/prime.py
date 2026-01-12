"""
File:prime.py
Author:CS1510
Description: Determines if a number is prime.
"""

###Get input number from user
##number = int(input("Please enter a number greater than 2. "))
##
###Set conditions
##isPrime = True #break out condition
##divisor = 2
##
###Divide number by divisors range 2 to number - 1. If
###prime, then no number will divide evenly.
##while divisor<number and isPrime:
##    if number%divisor==0:
##        print("The number",number,"is divisible by",\
##              divisor)
##        isPrime=False   # Going to break out
##    divisor=divisor+1
##
###Print if result is prime
##if isPrime:
##    print("That number is prime")
##else:
##    print("That number is NOT prime")

def isPrime(number):
    
    for divisor in range(2,number):
        if number%divisor==0:
            return False

    return True


        
    
