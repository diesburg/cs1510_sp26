"""
Lab09 Solutions
"""
def myCount(myList,item):
    count = 0

    for thing in myList:
        if thing == item:
            count += 1
    
    return count

def myIndex(myList,item):
    index = 0

    for thing in myList:
        if thing == item:
            return index
        index += 1

    return -1

###   Alternate way
##    for index in range(len(myList)):
##        if myList[index]==item:
##            return index
##
##    return -1

def contains(myList,item):

    for thing in myList:
        if thing == item:
            return True
    #Didn't return, so didn't find item
    return False

def myInsert(myList,index,item):

    #Check bad case
    if index < 0:
        return myList

    # Use slicing
    #return myList[:index] + [item] + myList[index:]

### Alternate way using loops
    outList = []

    #Copy everything into the new list before index
    for position in range(index):
    	outList.append(myList[position])
    
    #Append the new item    
    outList.append(item)

    #Copy everything into the new list after index
    for position in range(index,len(myList)):
        outList.append(myList[position])

    return outList
        

        

        
