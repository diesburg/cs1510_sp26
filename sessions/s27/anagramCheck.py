#Function anagramCheck
#Inputs: two words (strings)
#Outputs: True if anagram, False otherwise
#Description: Checks if two words are anagrams.

def anagramCheck(w1,w2):
    wordList1=list()
    wordList2=[]


    #How else could we put the characters of the words
    #into lists?
    for char in w1:
        wordList1.append(char)
    for char in w2:
        wordList2.append(char)



    print (wordList1)
    print (wordList2)
    
    wordList1.sort()
    wordList2.sort()
    
    print (wordList1)
    print (wordList2)

    if wordList1==wordList2  :
        return True
    else:
        return False


