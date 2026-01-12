'''
Program: allShiftsEncoding.py
Author: CS 1510
Description: Encode "PANTHERS" with every possible Caesar Cypher key using
the shifted string for that secret key (of 1, 2, 3, ..., or 25)
'''

inputStr = "PANTHERS"

#Original alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet.upper()
spaces = "   "

#Shifted alphabet
for rotation in range(1,27):
    shift = alphabet[rotation:] + alphabet[:rotation]

    encodedStr =""
