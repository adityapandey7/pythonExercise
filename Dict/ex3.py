# Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements from the second list become values.

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dictionary = {}

for i in range(len(keys)):
    new_dictionary.update({keys[i]: values[i]})

print(new_dictionary)