# While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.

# Write a Python program to check if the value 200 is present in the provided dictionary.

# Given:

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:

# 200 present in a dict

sample_dict = {'a': 100, 'b': 200, 'c': 300}

x = sample_dict.values()

if 200 in x:
    print(f" 200 is present")
else:
    print(f" 200 is not present")