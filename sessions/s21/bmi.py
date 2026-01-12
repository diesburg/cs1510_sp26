'''
File: bmi.py
Author: CS 1510
Description: Computes and prints bmi based on inputs from the user.
'''

weightStr = input("Please enter your weight in pounds. ")
heightStr = input("Please enter your height in inches. ")

weightKG = float(weightStr)* 0.453592
heightMeters = float(heightStr)*2.54/100

bmi = weightKG/(heightMeters)**2

print("Your BMI is "+str(bmi))
