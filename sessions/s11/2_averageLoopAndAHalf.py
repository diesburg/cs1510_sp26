"""
File : averageLoopAndAHAlf.py
Author : CS 1510
Description : Calculates the average score for a set of scores
        The user enters a -1 to signal that they are done
        entering scores.
        This version actually asks the question twice -
            1) Just outside the loop to give it a starting value
            2) Then at the END of the loop
        This version means you don't have to adjust.
"""


print("Enter the scores one at at a time.")
print("Enter -1 to signal that you are done.")

sumOfScores = 0
totalQuizzes = 0

score = int(input("Please enter a score: "))

while score!=-1:
    sumOfScores += score
    totalQuizzes = totalQuizzes +1
    score = int(input("Please enter a score: "))

average = sumOfScores/totalQuizzes
print("Your average on",totalQuizzes,"quizzes is",average)
