"""
Title:   prizeMoney.py
Author:   Sarah Diesburg
Comment:  Calculates athlete prize money based on
    the number of gold, silver, and bronze medals
    that they win in the olympics.
Deadline : ONTIME

"""

#Identify the prize money for each medal type 
GOLD_PRIZE = 25000
SILVER_PRIZE = 15000
BRONZE_PRIZE = 10000

#Obtain the number of gold, silver, and bronze medals for the athlete
goldMedals = input("How many gold medals? ")
silverMedals = input('How many silver medals? ')
bronzeMedals = input("How many bronze medals? ")

gold = int(goldMedals)
silver = int(silverMedals)
bronze = int(bronzeMedals)

#For each medal type, multiply the medal count with it’s prize amount.
#Sum these three values to get total money won.
total = gold*GOLD_PRIZE + silver*SILVER_PRIZE + bronze*BRONZE_PRIZE

#Display total amount of money won
print("This athlete has won $",total)


