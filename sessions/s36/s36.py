
#Global lists to illustrate concepts
ordered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

reverse = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

shuffle = [8, 12, 11, 2, 15, 20, 16, 18, 17, 9, 3, 5, 1, 4, 10, 6, 14, 7, 13, 19]

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

random = [75, 92, 57, 25, 31, 73, 30, 83, 88, 26, 2, 71, 22, 82, 22, 72, 70, 82, 14, 42]

def linearSearch(lyst,what):
    """Demonstrates a linear search"""
    length=len(lyst)

    #Search the entire list one at a time
    for index in range(0,length):
        if lyst[index]==what:
            return index

    #If we didn't find it in the list, return
    #something (either -1 or None)
    return -1


def binarySearch(lyst,what):
    """Demonstrates a binary search"""
    lowIndex = 0
    highIndex = len(lyst)-1


    while lowIndex<=highIndex  :
        middle = (lowIndex + highIndex)//2

        if lyst[middle]==what:
            return middle
        if lyst[middle]>what:
            highIndex=middle-1
        if lyst[middle]<what:
            lowIndex=middle+1
    
    return -1
    
    









    
