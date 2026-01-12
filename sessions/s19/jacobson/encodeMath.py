"""
Program: mathEncoding.py
Author: CS1510 and Mark Jacobson
Description: Caesar Cypher encoding using the ord()/chr() math method
"""

#Enter input
inputStr = input("Please enter string to encode ")
rotation = int(input("Please enter rotation "))

#Empty output string so you can build the output one
#character at a time
cipherText = ""

for ch in inputStr:

    #If it is a lowercase letter
    if ord(ch) >= 97 and ord(ch) <= 122:
        code = ord(ch)
        code = code + rotation

        #If we rotate too far (beyond z), subtract 26
        if code > 122:
            code = code - 26
        cipherText = cipherText + chr(code)

    #Not a lowercase letter
    else:
        cipherText = cipherText + ch

#Output the encoded string we built
print(cipherText)
