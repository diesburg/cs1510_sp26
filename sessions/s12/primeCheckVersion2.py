"""
File : primeCheck.py
Author : Diesburg
Description : Is the input prime?
"""

# Let's check all the numbers in range(2,100) for primeness

for number in range(2,100):

    isPrime = True #break out condition

    #for divisor in range(2,number):
    divisor = 2
    while divisor<number and isPrime:
        if number%divisor==0:
            isPrime=False
            #break
        divisor=divisor+1

    # And the verdict is...
    if isPrime:
        print(number,"is prime")
    else:
        print(number,"is NOT prime")
