"""
Program: leftTriangle.py
Author: CS 1510
Description: Prints a left-justified right triangle of stars, with a height based
on user input.
"""

#Input validation

height = int(input("Please input a positive height: "))

while(height < 1):
    height = int(input("Please input a positive height: "))


# Print the triangle

for row in range(1, height+1):
    for star in range(row):
        print("*",end=' ')
    print()

