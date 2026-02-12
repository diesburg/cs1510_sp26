"""
File : quiz.py
Author : Diesburg
Description : Calculates the average score for N scores
        where N is provided as input by the user.

        This version is broken.
"""

numberOfQuizzes = int( input("Enter the number of quizzes: "))

total = 0

for quizNumber in range(1,numberOfQuizzes):
    score = int(input("Enter the score on quiz " + str(quizNumber) + ": "))
    total = total + score

average = total/numberOfQuizzes
print("The average quiz score is " + str(average))



