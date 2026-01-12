"""
findCharacter.py
"""

# Write a program that 1) asks for a string, 2) asks for a character, and
# 3) finds that character's location in the string WITHOUT using the
# string find/index methods.

myString = input("Enter a string: ")
target = input("Input character to find: ")
found = False
for index in range(len(myString)): #for each index
    if myString[index] == target:  #check 
        print( "Letter found at index: ", index )
        found = True
        break                 # stop searching
if (found == False):
   print( 'Letter',target,'not found in',myString)


# Can you write a program that asks for a sentence, counts all the capital
# letters in the sentence, and prints that number to the user?
