"""
Program: rightTriangle.py
Author: CS 1510
Description: Prints a right-justified right triangle of stars, with a height based
on user input.
"""

#Input validation

height = int(input("Please input a positive height: "))

while(height < 1):
    height = int(input("Please input a positive height: "))


#Right-justified triangle
        
spaces = height
stars = 0


for currHeight in range(1, height+1):

    spaces -= 1
    stars += 1

    for spacesRow in range(spaces):
        print(" ",end=' ')

    for starsRow in range(stars):
        print("*",end=' ')

    print()


