"""
File : passWith.py
Author : Sarah Diesburg
Description : calculates the student's percentage and prints a message
  about whether they can move on to
  data structures based on a passing percentage
"""

#Constants
PASSING_PERCENT = 72
PERCENT_SHIFT = 100

#Get the total points possible from the user
totalString = input("How many total points were possible in the " \
                    "entire class? ")
totalInteger = int(totalString)

#Get the number of points earned from the user
earnedString = input("How many points did you earn? ")
earnedInteger = int(earnedString)

#Calculate and display the user's percentage
totalStudentPercentEarned = (earnedInteger/totalInteger) * \
                            PERCENT_SHIFT
print("That is",str(totalStudentPercentEarned)+"%")

#Determine and print if the user can enroll in data structures
if totalStudentPercentEarned>PASSING_PERCENT:  
    print("You can enroll in data structures")

    # Nice comment
    print("Fantastic Job")
    
else:
    print("You should retake CS1")
    

