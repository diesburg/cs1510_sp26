'''
File: setWordFrequency.py
Author: CS 1510
Description: This is yet another way to get the unique words from a file
using the data structure called a "set".  A Python set works much like
a mathematical set.
'''

def countWords(filename):

    # Open file, grab the contents, and close the file
    fin = open(filename,"r")
    contents = fin.read()
    fin.close()

    # Clean up the words
    contents = contents.lower()
    contents=contents.replace("\n"," ")
    contents=contents.replace(".","")
    contents=contents.replace(",","")
    contents=contents.replace("!","")
    contents=contents.replace("?","")
    contents=contents.replace("-"," ")

    # Get list of words
    words = contents.split()

    # Create empty set, add all words in list to set
    allWords = set()

    for word in words:
        allWords.add(word)
    
    # Return set
    return allWords
        
