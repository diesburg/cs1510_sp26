def createWordList(textFile):

    #Open the input file
    myFile = open(textFile,"r")

    #Read the file
    fileText = myFile.read()

    #Close the file
    myFile.close()

    #Clean up the test
    badChars = ".,!?;(){}:"

    for badChar in badChars:
        fileText=fileText.replace(badChar,"")

    #Deal with the dash
    fileText = fileText.replace("-"," ")

    #Lowercase all words
    fileText = fileText.lower()

    listOfWords = fileText.split()

    return(listOfWords)

def countUniqueWords(textFile):
    # Get the big word list
    wordList = createWordList(textFile)

    # Unique word list
    uniqueWordList = []

    for word in wordList:
        #If not in unique list
        if not word in uniqueWordList:
            uniqueWordList.append(word)

    return len(uniqueWordList)

def countWordFrequencies(textFile):
    # Get the big word list
    wordList = createWordList(textFile)

    # Make a word dictionary
    wordDict = {}

    # Go through each word in cleaned word list
    for word in wordList:

        #If it ISN'T in the dictionary already, put it in with
        #a count of 1
        if word not in wordDict:
            wordDict[word] = 1

        #If it IS in the dictionary, just add 1 to the value
        else:
            wordDict[word] += 1

    #print(wordDict)

        
    #Make a list of keys in the dictionary
    keyList=[]

    for word in wordDict:
        keyList.append(word)

    #Sort the list of keys
    keyList.sort()

    #Use the list of keys to print things out in order
    for word in keyList:
        print(word, wordDict[word])


    print()
    print()
    #####################################
    #Sort by value!

    masterList = []

    #Go through the dictionary, get out both the word and count
    #Add it to my masterList as a smaller mini list

    for word in wordDict:
        count = wordDict[word]
        miniList = [count,word]
        masterList.append(miniList)

    masterList.sort()
    masterList.reverse()

    #Go through sorted masterList, printing out count and word
    for miniList in masterList:
        print(miniList[0],miniList[1])





    

        










   
