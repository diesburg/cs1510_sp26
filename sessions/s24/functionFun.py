def addNumbers(num1,num2):
    '''Adds two numbers together and returns result'''

    #error checking
    if type(num1) != int or type(num2) != int:
        return None

    return num1+num2

def addNumToSelf(num1):
    '''Adds number to itself and returns result'''

    # This function calls another function...
    return addNumbers(num1,num1)


#Running the main part of the program
mySum = addNumToSelf(4)

#What should mySum be now?
print("mySum is", mySum)
