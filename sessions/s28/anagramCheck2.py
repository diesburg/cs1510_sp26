#Function anagramCheck
#Inputs: two words (strings)
#Outputs: True if anagram, False otherwise
#Description: Checks if two words are anagrams. This version uses sorted().

def anagramCheck(word1,word2):
    
    #Convert our strings into sorted lists
    wordList1=sorted(word1)
    wordList2=sorted(word2)
    
    #If the lists are the same, they are anagrams
    if wordList1==wordList2  :
        return True
    else:
        return False


