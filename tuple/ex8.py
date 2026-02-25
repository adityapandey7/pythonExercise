# Given a tuple of numbers, create a new tuple where each number is squared.

# Given:

# t = (1, 2, 3, 4)
# Expected Output:

# Original tuple: (1, 2, 3, 4)
# Squared tuple:  (1, 4, 9, 16)

t = (1, 2, 3, 4)
result = []

for item in t:
    result.append(item*item)

print(f"new tuple {tuple(result)}")