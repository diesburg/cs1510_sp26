'''
File: letterCount.py
Author: CS 1510
Description: Prints a table of the counts of each letter in a string.
This basic code can be tweaked to work with words in a text file or
fields in a csv.
'''

#Function letterCount
#Inputs: inputStr (string)
#Outputs: None
#Description: Prints a table of the letters of the alphabet (in
#   alphabetical order) together with the number of times each letter
#   occurs in inputStr.

def letterCount(inputStr):

    freq={}

    #Go through our sentence, adding one to our dictionary for
    #each letter we find
    for letter in inputStr:
            if letter not in freq:
                freq[letter] = 1
            else:
                freq[letter] += 1

    #At this point we have a working freq dictionary!  If we print it now,
    #then it will look weird.  Let's print it nicely, sorted by key.

    #Step 1 - Get a list of keys.
    key_list = []

    for key in freq:
        key_list.append(key)

    #Step 2 - Sort alphabetically (or ascending) by key
    key_list.sort()

    #Step 3 - Print it nicely, using a for loop to go through each key
    #in our sorted list.

    for key in key_list:
        value = freq[key] #Look up the value in the dictionary with the
                          #key we've got.
        print(key,value) 

    
    




