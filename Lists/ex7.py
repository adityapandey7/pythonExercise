# Write a function to flatten a list of lists into a single, non-nested list. (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4]).

# Given:

# list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
# Expected Output:

# [1, 2, 3, 4, 5, 6, 7]

list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
new_list = []


for sub_list in list_of_lists:
    for item in sub_list:
        new_list.append(item)

print(f"new list {new_list}")
