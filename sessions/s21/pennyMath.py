"""
Program: pennyMath.py
Author: CS 1510
Description: Calculates the penny math value of a string.
"""

# Get the input string
original = input("Enter a string to get its cost in penny math: ")

# Lowercase the text because capital and lowercase letters are counted
# the same in pennymath

original = original.lower()

cost = 0

# We make an alphabet string.  Indexes start at 0, so a is at 0.
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Go through each character in the input string
for char in original:
    
    if char>="a" and char<="z":
        index = alphabet.find(char)
        char_cost = index + 1 #alphabet indexes start at 0, so add 1
        cost += char_cost #add onto our cost tally
   

print("The cost of",original,"is",cost)

