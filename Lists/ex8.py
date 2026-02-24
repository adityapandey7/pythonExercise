# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given:

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output:

# ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Use the length of the longer list to avoid missing elements
max_len = max(len(list1), len(list2))
result = []

for i in range(max_len):
    # Get items if they exist, otherwise use an empty string
    item1 = list1[i] if i < len(list1) else ""
    item2 = list2[i] if i < len(list2) else ""
    
    result.append(item1 + item2)

print(result)


