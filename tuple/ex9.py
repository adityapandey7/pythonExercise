# Sort a tuple of tuples by 2nd item
# Given:

# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# Expected output:

# (Sorted tuple by 2nd item: (('c', 11), ('a', 23), ('d', 29), ('b', 37))

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

sorted_tuple = sorted(tuple1, key=lambda x:x[1])

print(f"sorted tuple: {tuple(sorted_tuple)}")