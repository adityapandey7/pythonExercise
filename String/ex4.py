# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

# Given:

# s1 = "America"
# s2 = "Japan"
# Expected Output:

# AJrpan

str1 = "America"
str2 = "Japan"

str1LengthMiddle = int(len(str1)/2)
str2LengthMiddle = int(len(str2)/2)

newString = str1[0]+str2[0] + str1[str1LengthMiddle] + str2[str2LengthMiddle] + str1[-1]+str2[-1]

print(newString)