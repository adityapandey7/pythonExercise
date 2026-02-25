# Compare two tuples and find out which one is “greater” and why?

# Given:

# t1 = (1, 2, 3)
# t2 = (1, 2, 4)
# Expected Output:

# Tuple 1: (1, 2, 3)
# Tuple 2: (1, 2, 4)
# (1, 2, 3) is less than (1, 2, 4)

t1 = (1, 2, 3)
t2 = (1, 2, 4)

if t1 > t2:
    print(f" tuple 1 is greater {t1} and {t2}")
elif t2 > t1:
    print(f" tuple 2 is greater {t1} and {t2}")
else:
    print("same")