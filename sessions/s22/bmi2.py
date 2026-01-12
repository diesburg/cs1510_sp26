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

    # athlete is a line (string) in the spreadsheet. We split it into
    # a list divided by commas.
    athlete_list = athlete.split(",")

    # Get the important columns by their index number in the spreadsheet.
    # Note: everything is a string and must be converted to float() or int()
    # if you want to do math with it.
    last = athlete_list[0]
    first = athlete_list[1]
    height = float(athlete_list[2])
    weight = float(athlete_list[3])

    # Weight needs to be converted to m instead of cm.  
    heightMeters = height/100

    # Figure out the bmi
    bmi = weight/(heightMeters)**2

    # Write it to the file.  All items must be strings, and we have to
    # add "\n" at the end.
    fout.write(last+","+first+","+str(bmi)+"\n")


# Close each spreadsheet    
fin.close()
fout.close()
    
