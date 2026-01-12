#Function anagramCheck
#Inputs: two words (strings)
#Outputs: True if anagram, False otherwise
#Description: Checks if two words are anagrams. This version uses
#             the list() constructor and the .sort() list method.

def anagramCheck(word1,word2):
    
    
    #Convert our strings into lists
    wordList1=list(word1)
    wordList2=list(word2)


    #Sort the list of characters in each word    
    wordList1.sort()
    wordList2.sort()
    
    #If the lists are the same, they are anagrams
    if wordList1==wordList2  :
        return True
    else:
        return False


