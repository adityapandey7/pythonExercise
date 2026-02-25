# Write a code to filter out students with scores less than 90 from a given a list of tuples.

# Given:

# students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# Expected Output:

# Students with scores 90 or above: [('Bob', 92), ('David', 95)]

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

result = []

for item in students:
   if item[1]>90:
      result.append(item)

print(f" pass student {result}")
