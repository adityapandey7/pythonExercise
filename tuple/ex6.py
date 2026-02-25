# Write a code to create a new tuple with only unique elements.

# Given:

# my_tuple = (1, 2, 2, 3, 4, 4, 5)
# Expected Output:

# Original tuple with duplicates: (1, 2, 2, 3, 4, 4, 5)
# Tuple with unique elements: (1, 2, 3, 4, 5)

# my_tuple = (1, 2, 2, 3, 4, 4, 5)

# new_tuple = tuple(set(my_tuple))

# print(f"new tuple: {new_tuple}")

# or

my_tuple = (1, 2, 2, 3, 4, 4, 5)
unique_list = []

for item in my_tuple:
    if item not in unique_list:
        unique_list.append(item)

unique_tuple = tuple(unique_list)
print(f"uniqque tuple {unique_tuple}")