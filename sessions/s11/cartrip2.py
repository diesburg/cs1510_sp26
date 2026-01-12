"""
File : cartrip.py
Author : Diesburg
Description : Prints "Are we there yet" multiple times
    This particular solution shows three different
    but comparable ways.
"""

"""

while loop (sentinel controlled loop, event controlled loop)

while BooleanConditionIsTrue:
    suite of code

"""

age = int(input("How old is the child? "))

#for loop
for counter in range(age):
          print("Are we there yet?")
print("Isn't it annoying to have a",age,"year old in the car")
print()
print("Let's print it again")
print()

#while loop counting up

counter=0
while counter<age:
    print("Are we there yet?")
    #counter=counter+1
    counter += 1
print("Isn't it annoying to have a",age,"year old in the car")
    
print()
print("Let's print it again")
print()

#while loop counting down

while age>0:
    print("Are we there yet?")
    age -= 1
print("Isn't it annoying to have a",age,"year old in the car")







