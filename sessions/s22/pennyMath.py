'''
File: pennyMathHard.py
Author: CS 1510
Description: Enter a word to compute the cost of the word.
'''

# Get the word from the user
original = input("Enter a string ")

cost = 0

# For each letter in the word, compute the cost.  Sum the
# cost of each letter into variable cost
for char in original:
    value = ord(char)
    if char>="a" and char<="z":
        cost = cost+(value-96)
    elif char>="A" and char<="Z":
        cost = cost+(value-64)
        
# Display results
print("The cost of",original,"is",cost)

