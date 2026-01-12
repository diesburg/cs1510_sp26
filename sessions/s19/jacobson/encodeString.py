"""
Program: encodeString.py
Author: CS1510 and Mark Jacobson
Description: Solution to encode using the Caesar Cypher and
string shifting.
"""

#Get inputs
inputStr = input("Please enter string to encode ")
rotation = int(input("Please enter rotation "))

#Create an alphabet string for lookups
alphabet = "abcdefghijklmnopqrstuvwxyz"

#Create a rotated alphabet string based on the rotation number
shifted = alphabet[rotation:] + alphabet[0:rotation]

#Output string that we build one character at a time
cipherText = ""

for ch in inputStr:

    #First, get the index of the letter to encode in the alphabet
    charIndex = alphabet.find(ch)

    #If the find method did not return -1, it is a lowercase letter
    #and we can encode it
    if charIndex >= 0:
       cipherText = cipherText + shifted[charIndex]
    else:
       cipherText = cipherText + ch

#Display output string we built
print(cipherText)
