'''
File: dollarWords
Author: CS 1510
Description: Uses a file dictionary to compute dollar words
based on penny math.  Opens a dictonary file and reads it line
by line.  Computes value and writes word to output file if it
is worth exactly 100 cents.
'''

# Open our files
fin = open("dictionary.txt","r")
fout = open("extracredit.txt","w")

#For every line, get each word
for original in fin:
    original = original[:-1] #Why this line?
    cost = 0

    #For every word, compute the penny math
    for char in original:
        value = ord(char)
        if char>="a" and char<="z":
            cost = cost+(value-96)
        elif char>="A" and char<="Z":
            cost = cost+(value-64)

    #Write dollar words to file
    if cost==100:
        fout.write(original+"\n")


print("Output file written called 'extracredit.txt'")

fin.close()
fout.close()
