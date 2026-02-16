# Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# Given:

# str1 = PyNaTive
# Expected Output:

# yaivePNT

str = "PyNaTive"
result = ""

for letter in str:
    if letter.islower():
        result += letter

for letter in str:
    if letter.isupper():
        result += letter

print(result)


