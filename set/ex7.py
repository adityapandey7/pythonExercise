# Check if set1 is a subset of set2. Write a code to return True if every element in the subset_set is also present in the main_set.

# Given:

# subset_set = {10, 20}
# main_set = {10, 20, 30, 40}

# method 1 

# subset_set = {10, 20}
# main_set = {10, 20, 30, 40}

# new_set = main_set.intersection(subset_set)

# if new_set == subset_set:
#     print(True)
# else:
#     print(False)

# method 2

subset_set = {10, 20}
main_set = {10, 20, 30, 40}

is_subset = subset_set.issubset(main_set)

print(is_subset)
