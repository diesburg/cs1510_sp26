'''
Program: nestedLoops.py
Author: CS1
Description: Nested loops got you down?  Then play with the basics!  Take a look
at each of these nested loop examples, and see if you can predict what will
be printed before they are run.
'''

# First example.  What will be printed?

for index in range(1,5):
    print(index)

    for index2 in range(1,4):
        print(index2)
    ### end inner loop

### end outer loop


# Second example.  What will be printed?
for index in range(2,4):

    for index2 in range(1,4):
        print(index, "+", index2, "=", (index+index2))

    ### end inner loop

    print("bananas!")

### end outer loop



