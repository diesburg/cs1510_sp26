"""
Program: forLoopWithStrings2.py
Description: Counts number of digits in bigN using strings
"""

bigN = input("Enter the big number: ")
digit = input("Search for this digit: ")

totalMatching = 0
length = len(bigN)

for number in range(0,length):
    char = bigN[number]
    if char == digit:
        totalMatching +=1


print(totalMatching)
