"""
Diesburg's solution to the number counter problem
"""

#Get input
val = input("What is the large number? ")
while not val.isdigit():
    val = input("What is the large number? ")
large = int(val)
original = large  #save a copy!


val = input("What is the single number? ")
while (not val.isdigit()) or  int(val)>9:
    val = input("What is the single number? ")
digit = int(val)
   

#Set counter to zero
count=0


#loop through the number one digit at a time
while large>0:
    singledigit = large%10
    if singledigit == digit: #is this the droid I am looking for?
        count = count+1
    large = large//10

#Print results
print("There were "+str(count)+\
      " occurences of "+str(digit)+ \
      " in "+str(original))
