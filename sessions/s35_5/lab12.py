def getStateDistribution():
    fin = open("FakeCustomerData.txt", "r")

    fin.readline()

    cust_dict = {}

    for customer in fin:
        customerList = customer.split(",")
        state = customerList[7]

        #dictionary
        if state not in cust_dict:
            cust_dict[state] = 1
        else:
            cust_dict[state] += 1



    keyList = list(cust_dict.keys())
    keyList.sort()
    #print(keyList)

    for key in keyList:
        print(key, cust_dict[key])

    fin.close()


def getColumnDistribution(filename, col):
    fin = open(filename, "r")

    fin.readline()

    cust_dict = {}

    for customer in fin:
        customerList = customer.split(",")
        state = customerList[col]

        #dictionary
        if state not in cust_dict:
            cust_dict[state] = 1
        else:
            cust_dict[state] += 1



    keyList = list(cust_dict.keys())
    keyList.sort()
    #print(keyList)

    for key in keyList:
        print(key, cust_dict[key])

    fin.close()




def getBirthYearDistribution():
    fin = open("FakeCustomerData.txt", "r")

    fin.readline()

    cust_dict = {}

    for customer in fin:
        customerList = customer.split(",")
        full_birthday = customerList[12]
        birthdayList = full_birthday.split("/")
        year = birthdayList[-1]

        #dictionary
        if year not in cust_dict:
            cust_dict[year] = 1
        else:
            cust_dict[year] += 1



    keyList = list(cust_dict.keys())
    keyList.sort()
    #print(keyList)

    for key in keyList:
        print(key, cust_dict[key])

    fin.close()
