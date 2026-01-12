"""
File : passWith.py
Author : CS1510
Description : calculates the student's percentage and
  prints a message about whether they can move on to
  data structures based on a passing cut off of 73%
"""

totalStr = input("How many total points were possible? ")
total = int(totalStr)
earnedStr = input("How many points did you earn? ")
earned = int(earnedStr)
percent = earned/total*100

print("That is",percent,"%")

if percent>73:  
    print("You can enroll in data structures")
print("Fantastic Job")
    

    
if percent<73:
    print("You should retake CS1")
    print("Too bad")



    

