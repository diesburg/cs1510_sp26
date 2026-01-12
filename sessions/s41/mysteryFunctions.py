'''
File: mysteryFunctions.py
Author: CS 1510
Description: Figure out two things about these mystery
functions to help you study for the test:
1) What data types can be passed in as the different parameters?
2) Overall, what is the mystery function doing?

Potential Data types
--------------------
        Integer
        String
        Float
        List
        Dictionary
        Set
        Tuple
        File
        Boolean
'''

#What types can parameter a be?
#What types can parameter b be?
#What is the function doing?

def mysteryFunction1(a,b):  
    for item in a:
        if item==b:
            return True
    return False



def mysteryFunction2(a,b):  
    output=[]
    while len(a)>0 and len(b)>0:
        if a[0]<b[0]:
            output.append(a[0])
            a.pop(0)
        else:
            output.append(b[0])
            b.pop(0)
    if len(a)>0:
        output.extend(a)
    else:
        output.extend(b)
    return output

