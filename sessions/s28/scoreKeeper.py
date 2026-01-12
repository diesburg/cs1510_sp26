"""
Program: scoreKeeper.py
Author: CS 1510
Description: Keeps a list of student names and scores
"""
#Function Name: scoreKeeper
#Inputs: Interactive function that asks user for student names and scores.
#        Takes no parameters.
#Outputs: Returns a master list of smaller lists of scores and names.
def scoreKeeper():
    """Interactive score keeper function that returns a master class list of scores/names"""
    
    print("Enter scores and names.  Enter -1 to quit.")

    #Make an empty list
    masterList = []

    keepGoing = True

    #Loop while keepGoing == True
    while keepGoing:
        score = float(input("Please enter the student's score: "))

        #If they entered -1, set keepGoing to False to stop the loop
        if score == -1:
            keepGoing = False

        #Otherwise, let's get the student's name and add both the score
        #and the name to the masterList
        else:
            name = input("Please enter the student's name: ")

            masterList.append([score,name]) #note the []!  We are appending
                                            #the score and name inside a
                                            #smaller list within masterList

    #After we are all done with the loop, return the list
    return masterList


        
