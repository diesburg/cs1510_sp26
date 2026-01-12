"""
encode
"""

text = input("Enter the text to encode: ")

# TA note: When prompting for the text, some students may be
# tempted to .lower() (lowercase) the text.  They shouldn't do
# this.  We are only encoding lowercase letters and leaving
# uppercase letters alone.

rotation = int(input("Enter the rotation (0-25): "))

alpha = "abcdefghijklmnopqrstuvwxyz"

result = ""

for char in text:

    # If lowercase letter, encode it!
    if char in alpha:
        index = alpha.find(char) + rotation #Step 1: use .find()

        # Wrap around code if we go too far
        if index > 25:
            index-=26
         
            
        result += alpha[index] #Step 2: use indexing

    # Otherwise not lowercase letter, so we leave it alone.
    else:
        result += char


print(result)


