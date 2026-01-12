"""
Program: forLoopWithStrings1.py
Description: Counts number of digits in bigN using strings
"""

bigN = input("Enter the big number: ")
digit = input("Search for this digit: ")

totalMatching = 0

for char in bigN:
    if char == digit:
        totalMatching +=1


print(totalMatching)
