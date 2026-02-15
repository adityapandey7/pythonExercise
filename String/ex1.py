# Create a string made of the first, middle and last character

# Write a program to create a new string made of an input string’s first, middle, and last character.

# Given:

# str1 = "James"
# Expected Output:

# Jms

name = input("enter the name")
length_of_name = len(name)
newName = name[0]+name[int(length_of_name/2)]+name[-1]

print(newName)