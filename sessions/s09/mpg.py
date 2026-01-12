"""
Program: mpg.py
Author: CS1510
Description: Figures out mpg of car using starting mileage, ending
mileage, and gas consumed.
"""

#Get starting and ending mileage, as well as gas consumed
startMileage = int(input("Enter starting mileage"))
endMileage = int(input("Enter ending mileage"))
gasConsumed = float(input("Enter gas consumed"))

#Calculate mpg
mpg = (endMileage - startMileage) / gasConsumed

#Print result
print("The mpg for your car is", mpg)
