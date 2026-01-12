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
    
    original = original.lower()

    cost = 0

    # We make an alphabet string.  Indexes start at 0, so a is at 0.
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Go through each character in the input string
    for char in original:
        
        if char>="a" and char<="z":
            index = alphabet.find(char)
            char_cost = index + 1 #alphabet indexes start at 0, so add 1
            cost += char_cost #add onto our cost tally

    #Write dollar words to file
    if cost==100:
        fout.write(original+"\n")


print("Output file written called 'extracredit.txt'")

fin.close()
fout.close()
