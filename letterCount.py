'''
File: letterCount.py
Author: CS 1510
Description: Prints a table of the counts of each letter in a string.
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

    #At this point we have a working freq dictionary!  However,
    #we want to sort it by frequency.  How?  We must make a list
    #of minilists that hold the [frequency, key] for each letter.
    

    #Step 1 - create the large list to hold the [frequency, key] pairs.

    big_list = []

    #Step 2 - go through the dictionary, getting each key and frequency.
    #Add them to a mini list and append to the big list.
    
    for letter in freq:
        mini_list = [freq[letter], letter]
        big_list.append(mini_list)

    #Step 3 - sort!  The mini lists will sort by the first items.
        
    big_list.sort(reverse=True)
 
    #Step 4 - pretty printing
    for mini_list in big_list:
        print(mini_list[1]," ",mini_list[0])
        

        
    




