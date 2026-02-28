# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
# Perform following operations on given dictionary

# Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
# Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
# Check if Key Exists in the dictionary
# Expected Output:

# Original dictionary: {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

# Updated dictionary after removing 'profession': {'name': 'Alice', 'age': 35, 'city': 'New York'}

# Printing all key-value pairs:
# name: Alice
# age: 35
# city: New York

# Does 'age' exist? True

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

my_dict.pop("profession")

print(f"remove {my_dict}")

print("print all key value")
for x,y in my_dict.items():
    print(f"{x} : {y} ")

if "age" in my_dict:
    print(f"does age present {True}")
else:
    print(f"does age presnet {False}")