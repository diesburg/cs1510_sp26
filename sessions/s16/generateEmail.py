'''
Name: generateEmail.py
Author: CS1
Description: Generate a UNI email address based on the first
5 characters of the last name and first 1 character of the first name
'''

#Get first and last name
first = input("Please enter the first name ")
last = input("Please enter the last name ")

#If last name doesn't have 5 characters, use what we have
if len(last)>4:
    email=last[0:5]
else:
    email=last

#Add first name and UNI postfix
email = email + first[0] + "@uni.edu"

#Display email
print (email)
