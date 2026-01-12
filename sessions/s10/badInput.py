"""
Program: badInput.py
Author: CS 1510
Description: Testing bad input.
"""

number = int(input("Input a number from 0-5: "))

while (number < 0) or (number > 5) :
    number = int(input("Input a number from 0-5: "))

print("Valid!")
