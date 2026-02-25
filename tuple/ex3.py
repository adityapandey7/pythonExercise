# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

# Given:

# tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:

# tuple2: (44, 55)

tuple1 = (11, 22, 33, 44, 55, 66)

new_tuple = tuple1[3:-1]

print(f"new tuple {new_tuple}")