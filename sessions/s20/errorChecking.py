'''
Program: errorChecking.py
Author: CS1
Description: Let's practice checking for errors with a while loop.
Take a look at these examples, then try to do them on your own!
'''

# How can we check for a positive integers?

number = int(input("First test: Enter positive integer "))

while(number <= 0):
    number = int(input("First test: Enter positive integer "))




# How can we check for an integer between -5 and 20,
# assuming the user enters numbers?

number = int(input("Second test: Enter an integer between -5 and 20: "))

while(number < -5 or numberStr > 20):
    number = int(input("Second test: Enter an integer between -5 and 20: "))


# How can we check for valid menu choices r, R, p, P, s, S, q, or Q?

choice = input("Enter r, p, s, or q: ")
choice = choice.lower()

while choice!= "r" and choice!= "p" and choice!= "s" and choice!="q":
    choice = input("Enter r, p, s, or q: ")
    choice = choice.lower()



