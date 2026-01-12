"""
File : averageCommon.py
Author : CS 1510
Description : Calculates the average score for a set of scores
        The user enters a -1 to signal that they are done
        entering scores.
        
        Since this version adds an extra score of negative one,
        we have to adjust for it at the end.
"""


print("Enter the scores one at at a time.")
print("Enter -1 to signal that you are done.")


sumOfScores = 0
totalQuizzes = 0

score=0 # Need to give it an initial value so it enters the loop

while score != -1:
    score = int(input("Please enter a score: "))
    sumOfScores = sumOfScores + score
    totalQuizzes = totalQuizzes +1

#Adjust the extra score of -1 by removing it.
sumOfScores += 1
totalQuizzes -= 1

average = sumOfScores/totalQuizzes
print("Your average on",totalQuizzes,"quizzes is",average)
