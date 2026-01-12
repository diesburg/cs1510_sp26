"""
File: tester.py
Author: Diesburg
Description: This file serves as a tester for lab09. Running this script
will automatically import all functions from your lab09.py file and test
them.

If you get a red error right away, your function names may not be named
exactly as I requested, and my tester will not be able to test your code.
"""

#This statement "imports" all functions in your lab09.py file so that they
#can be called from this file.
from lab09 import *

def checkResults(actual,expected,function):
    """check the results of a function you created"""
    if actual!=expected:
        print(function,"was supposed to return",expected,"but returned",actual)
    return None

#Actual tester program starts here
print("Start checking for errors")

data = [1,2,3,1,2,4,1,4,5]

#Checking myCount function
checkResults(myCount(data,1),3,"myCount")
checkResults(myCount(data,2),2,"myCount")
checkResults(myCount(data,5),1,"myCount")
checkResults(myCount(data,6),0,"myCount")

#Checking myIndex function
checkResults(myIndex(data,1),0,"myIndex")
checkResults(myIndex(data,5),8,"myIndex")
checkResults(myIndex(data,6),-1,"myIndex")

#Checking contains function
checkResults(contains(data,1),True,"contains")
checkResults(contains(data,5),True,"contains")
checkResults(contains(data,6),False,"contains")

#Checking myInsert function
data = []
copy = []
copy.insert(0,"apple")
checkResults(myInsert(data,0,"apple"),copy,"myInsert")

data = [1,2,3,1,2,4,1,4,5]
copy = data[:]
copy.insert(0,2)
checkResults(myInsert(data,0,2),copy,"myInsert")

data = [1,2,3,1,2,4,1,4,5]
copy = data[:]
copy.insert(9,2)
checkResults(myInsert(data,9,2),copy,"myInsert")

data = [1,2,3,1,2,4,1,4,5]
copy = data[:]
copy.insert(4,2)
checkResults(myInsert(data,4,2),copy,"myInsert")



print("Done checking for errors")

