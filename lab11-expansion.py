"""
File: lab11.py
Author: Diesburg
Description: Reads FakeCustomerData.txt and extracts frequency info based on columns.
"""
       
##def getColumnDistribution(filename,columnNum):
##    """Given a filename and column number, print frequencies sorted by key."""
##    
##    fin = open(filename, 'r')
##    header = fin.readline()
##
##    if columnNum > len(header.split(',')):
##        print('There is no column number', columnNum)
##        return
##
##    customerDict = {}
##
##    for line in fin:
##        listSplit = line.split(',')
## 
##        #not working if index out of range
##        data = listSplit[columnNum]
##        if data in customerDict:
##            customerDict[data] +=1
##        else:
##            customerDict[data] = 1
##
##    key_list = list(customerDict.keys())
##    key_list.sort()
##
##    for data in key_list:
##        print(data, '->',customerDict[data])

###

def getColumnDistribution(filename,columnNum,sortType):
    """Given a filename and column number, print frequencies sorted by sortType ("key" or "value")."""
    
    if sortType.lower() != "key" and sortType.lower() != "value":
        print("Please use sortType 'key' or 'value'.  Quitting.\n")
        return None

    fin = open(filename, 'r')
    header = fin.readline()

    if columnNum > len(header.split(',')):
        print('There is no column number', columnNum)
        return

    customerDict = {}

    for line in fin:
        listSplit = line.split(',')
 
        #not working if index out of range
        data = listSplit[columnNum]
        if data in customerDict:
            customerDict[data] +=1
        else:
            customerDict[data] = 1
    
    if sortType.lower() == "key":
        keySort(customerDict)
    else:
        valueSort(customerDict)

def keySort(customerDict):

    key_list = list(customerDict.keys())
    key_list.sort()

    for key in key_list:
        print(key, '->',customerDict[key])

def valueSort(customerDict):

    master_list = []

    for key,value in customerDict.items():
        mini_list = [value,key]
        master_list.append(mini_list)

    master_list.sort()
    master_list.reverse()

    for value,key in master_list:
        print(key, '->',value)

    

