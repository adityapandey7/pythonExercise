# Write a function that takes a list with duplicate elements and returns a new list with only unique elements.

# Given: list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

# Expected Output:

# [1, 2, 3, 4, 5]

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
new_list = []

def remove_duplicates(mylist):
    for i in mylist:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    
    print(f"new list {new_list}")

remove_duplicates(list_with_duplicates)