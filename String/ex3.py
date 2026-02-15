#  Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

# Given:

# s1 = "Ault"
# s2 = "Kelly"
# Expected Output:

# AuKellylt

str1 = input("enter str1")
str2 = input("enter str2")

middleOfStr1 = int(len(str1)/2)

x = str1[:middleOfStr1]
y = x+str2
newStr = y+str1[middleOfStr1:]

print(newStr)
