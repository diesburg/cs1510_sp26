"""
Program: pennyMath.py
Author: CS 1510
Description: Calculates the penny math value of a string.
"""

# Get the input string
original = input("Enter a string to get its cost in penny math: ")

cost = 0

# Go through each character in the input string
for char in original:
    
    value = ord(char)  #ord() gives us the encoded number!

    if char>="a" and char<="z":
        cost = cost+(value-96)    #offset the value of ord by 96
    elif char>="A" and char<="Z":
        cost = cost+(value-64)    #offset the value of ord by 64

print("The cost of",original,"is",cost)

