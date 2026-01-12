'''
Program: encodeMath.py
Author: CS 1510
Description: Encode a string with the Caesar Cypher using the
mathematical way
'''

inputStr = input("Please enter string to encode ")
rotation = int(input("Please enter rotation "))

encodedStr =""

for char in inputStr:

    # Encoding case
    if char >= 'a' and char <= 'z':
        encodedOrdChar = ord(char) + rotation

        #Have we gone over our bounds?
        if encodedOrdChar > ord('z'):
            encodedOrdChar = encodedOrdChar - 26 #fix it

        #Build our output string
        encodedStr = encodedStr + chr(encodedOrdChar)

    # Not encoding
    else:
        encodedStr = encodedStr + char


# Display our encoded string            
print(encodedStr)

    

               
