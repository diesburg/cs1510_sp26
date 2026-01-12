'''
Program: reverse2.py
Author: Sarah Diesburg
Description: Another way to reverse a line of text
'''

# Get the text from the user
text = input("Enter the text you would like to switch ")
result = ""
length = len(text)

for index in range(1,length+1):
    result = result + text[-index] #Build from left to right

# Results
print("original - "+text)
print("reversed - "+result)
