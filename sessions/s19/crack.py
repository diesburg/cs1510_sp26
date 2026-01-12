"""
Crack
"""

text = input("Enter the text to decode: ")

text_to_find = input("Enter a word that appears in the decoded text: ")

alpha = "abcdefghijklmnopqrstuvwxyz"

# Try all rotations between 0-25
for rotation in range(0,26):

    result = ""

    for char in text:

        # If lowercase letter, decode it!
        if char in alpha:
            index = alpha.find(char) - rotation # Step 1: use .find()

            # Wrap around code if we go too far
            if index < 0:
                index+=26
                
            result += alpha[index] #Step 2: use indexing

        # Otherwise not lowercase letter, so we leave it alone.
        else:
            result += char


    # Does the text_to_find exist in the result string?
    if result.find(text_to_find) != -1:

        #We found it!
        print("Decoded text:", result)
        print("Rotation:", rotation)

        break  #Stop


