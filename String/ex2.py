# Write a program to create a new string made of the middle three characters of an input string.

# Given:

# Case 1

# str1 = "JhonDipPeta"
# Output

# Dip
# Case 2

# str2 = "JaSonAy"
# Output

# Son

name = input("enter a name")

lengthOfName = len(name)

middleLength = int(lengthOfName/2)

newName = name[middleLength-1:middleLength+2]

print(newName)