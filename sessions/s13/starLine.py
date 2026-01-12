"""
Program: starLine.py
Author: CS 1510
Description: Prints a line of stars
"""

number = int(input("Please input a positive number: "))

while(number < 1):
    number = int(input("Please input a positive number: "))

for star in range(number):
    print("*",end=' ')

print()
