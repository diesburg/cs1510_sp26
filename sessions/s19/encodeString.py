'''
Program: encodeString.py
Author: CS 1510
Description: Encode a string with the Caesar Cypher using a
shifted string
'''

inputStr = input("Please enter string to encode ")
rotation = int(input("Please enter rotation "))

encodedStr =""

#Original alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

#Shifted alphabet
shift = alphabet[rotation:] + alphabet[:rotation]


for char in inputStr:

    # Encoding case
    if char in alphabet:
        position = alphabet.find(char)
        encodedChar = shift[position]
        encodedStr = encodedStr + encodedChar

    # Not encoding
    else:
        encodedStr = encodedStr + char

# Display our encoded string            
print(encodedStr)

    

               
