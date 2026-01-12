'''
Program: reverse.py
'''

text = input("Enter the text you would like to switch ")

result = ""

for char in text:
    result = char +result

print("original - "+text)
print("reversed - "+result)

