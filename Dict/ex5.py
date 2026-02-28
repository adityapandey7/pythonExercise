# Given a string, create a dictionary where keys are characters and values are their frequencies in the string.

# Given:

# string1 = 'Jessa'
# Expected Output:

# Frequencies for 'Jessa': {'J': 1, 'e': 1, 's': 2, 'a': 1}

string1 = 'Jessa'

dict1 = {}

for i in string1:
    dict1.update({i:string1.count(i)})

print(dict1)