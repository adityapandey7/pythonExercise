# Write a program to find words with both alphabets and numbers from an input string.

# Given:

# str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output:

# Emma25
# scientist50

str1 = "Emma25 is Data scientist50 and AI Expert"

words = str1.split()
newList = []

for item in words:
    has_alpha = False
    has_digit = False
    
    for char in item:
        if char.isalpha():
            has_alpha = True
        if char.isdigit():
            has_digit = True
    
    if has_alpha and has_digit:
        newList.append(item)

for i in newList:
    print("new List", i)

