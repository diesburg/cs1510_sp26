'''
File:bmi2.py
Author: CS 1510
Description: We modify our previous bmi program by reading in a
CSV (comma separated value) spreadsheet file.
'''

# Create our input and output files
fin = open("athletes_data.csv","r")
fout = open("athlete_bmi.csv","w")

# Write a header to the output file
fout.write("Last,First,BMI\n")

# Read the header from the input file (it contains no usable data)
header = fin.readline()

# For each line (athlete) in the input file: split up the information into
# usable chunks, compute the bmi, and write the information to the otuput
# spreadsheet file in CSV format
for athlete in fin:
    last,first,height,weight,country,gender,sport=athlete.split(",")

    weightKG = float(weight)
    heightMeters = float(height)/100
    
    bmi = weightKG/(heightMeters)**2
    fout.write(last+","+first+","+str(bmi)+"\n")


# Close each spreadsheet    
fin.close()
fout.close()
    
