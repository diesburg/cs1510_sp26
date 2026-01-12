original = input("Enter a string ")

cost = 0

for char in original:
    value = ord(char)
    if char>="a" and char<="z":
        cost = cost+(value-96)
    elif char>="A" and char<="Z":
        cost = cost+(value-64)

print("The cost of",original,"is",cost)

