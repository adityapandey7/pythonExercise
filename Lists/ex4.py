# Find and print the largest and smallest number in a list [8, 2, 15, 1, 9].

# Given:

# data = [8, 2, 15, 1, 9]
# Expected Output:

# Largest number: 15
# Smallest number: 1

data = [8,2,15,1,9]
data.sort()

print(f"smallest {data[0]}")
print(f"largest {data[-1]}")

# we can also use data.min() and data.max() function

