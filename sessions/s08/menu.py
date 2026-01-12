"""
Name: menu.py
Author: Sarah Diesburg
Description: Simple menu-driven program to illustrate if/elif/else.
"""

# Get a menu choice from the user
menuChoiceStr = input("Please enter a menu choice 1-3: ")
menuChoiceInt = int(menuChoiceStr)

# Print out the user's choice
if menuChoiceInt == 1:
    print("You got chicken.")
elif menuChoiceInt == 2:
    print("You got eggs.")
elif menuChoiceInt == 3:
    print("You got scraps.")
else:
    print("You didn't enter a valid number!!")
