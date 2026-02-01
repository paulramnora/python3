# Program: Get user first/last/middle name...
#          then, print out name specially formatted:
#          Full name: fName mName lName
#          First and last name; fName lName
#          Initials: lName[0]. mName[0]. LName[0].

# input...

fName=input("Enter first name: ")
mName=input("Enter middle name: ")
lName=input("Enter last name: ")

# output...

print() # prints a blank vertical line...for clearer output spacking.

print(f"Your full name is: {fName} {mName} {lName}")
print(f"Your first and last name are: {fName} {lName}")
print(f"Your initials are: {fName[0]}. {mName[0]}. {lName[0]}.") 
