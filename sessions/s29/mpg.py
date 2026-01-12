def driveInIowa(mpg):
    print("You can drive in Iowa")

def driveInCalifornia(mpg):
    if mpg < 35:
        print("You cannot drive in California")
    else:
        print("You can drive in California")

def calculateMPG(starting, ending, gasConsumed):
    return (ending-starting)/gasConsumed

def getData():
    starting = int(input("What is your starting mileage?"))
    ending = int(input("What is your ending mileage? "))
    gasConsumed = int(input("What is your gas consumed? "))

    return starting,ending,gasConsumed

def printData(mpg):
    print("Your mpg is:",mpg)
    driveInCalifornia(mpg)
    driveInIowa(mpg)


#function: main
#inputs: from command line: starting mileage (int), ending
#mileage (int), gas consumed (int)
#outputs: prints mpg and if can drive in California
#Description: This function determines mpg and drivability in California
def main():
    #Get data
    starting,ending,gasConsumed = getData()
    
    #Calculate MPG
    mpg = calculateMPG(starting,ending,gasConsumed)

    #Print Data
    printData(mpg)
   

