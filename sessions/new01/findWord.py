
# Ask the user for a word

# Search through a document

# How many times the word occurs  ##counter (integer)

# Tell us what line numbers we can find the word in  # list [1,2,10,...]

#-----------------

#write a function that: takes in word and a file

#------------------

def findWord(word,filename):

    counter = 0
    lineCounter = 0
    lineList = []

    # open the file??
    fin = open(filename,"r")


    # read the file, line by line
    for line in fin:

        lineCounter += 1       


        #get words out of the line
        wordList = line.split()
        print(wordList)

        #go through each word
        for thing in wordList:

            #if the word matches what we are looking for
            if thing == word:
                # add 1 to a counter
                counter = counter + 1
                # add the line number to the line list
                lineList.append(lineCounter)


    #print out counter and line list
    print("The word appeared this many times:", counter)
    print(lineList)
    
    fin.close()   

