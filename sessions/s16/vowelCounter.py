'''
Program: vowelCounter.py
Author: CS1
Description: Counts the number of different vowels
in a string
'''

#Get the string
original = input("Enter a string ")

#Convert the string to lowercase so matching is easier
original = original.lower()

#Set our counters
numAs = 0
numIs = 0
numEs = 0
numOs = 0
numUs = 0

#For each letter, count the number of vowels
for char in original:
    if char=="a" :
        numAs = numAs +1
    elif char=="e":
        numEs = numEs +1
    elif char=="i":
        numIs = numIs +1
    elif char=="o":
        numOs = numOs +1
    elif char=="u":
        numUs = numUs +1

#Display the results
print(numAs,numEs,numIs,numOs,numUs)
