# Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.

# Given:

# def get_min_max(numbers):
#     # Write your code here

# # Test the function
# my_numbers = [10, 5, 20, 2, 15]
# min_max_values = get_min_max(my_numbers)
# print(f"Original numbers: {my_numbers}")
# print(f"Minimum and maximum values: {min_max_values}")
# Expected Output:

# Original numbers: [10, 5, 20, 2, 15]
# Minimum and maximum values: (2, 20)



def get_min_max(numbers):
    min_val = min(numbers)
    max_val = max(numbers)

    return (min_val, max_val)
# Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")