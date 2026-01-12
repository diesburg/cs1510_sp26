"""
File : averageInfiniteBreak.py
Author : CS 1510
Description : Calculates the average score for a set of scores
        The user enters a -1 to signal that they are done
        entering scores.
        This version enters an infinite loop and uses the "break" 
        statement to get out when the stopping condition is met.
"""


print("Enter the scores one at at a time.")
print("Enter -1 to signal that you are done.")

sumOfScores = 0
totalQuizzes = 0

keepGoing = True

while keepGoing:
    score = int(input("Please enter a score: "))
    if score == -1:
        keepGoing = False
    else:
        sumOfScores += score
        totalQuizzes = totalQuizzes +1

if totalQuizzes==0:
    print("You didn't give me any data")
else:
    average = sumOfScores/totalQuizzes
    print("Your average on",totalQuizzes,"quizzes is",average)










