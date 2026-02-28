# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
# Perform following operations on given dictionary

# Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
# Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
# Access Key: Print the value associated with the city key.
# Expected Output:

# Original dictionary: {'name': 'Alice', 'age': 35, 'city': 'New York'}

# Updated dictionary after adding 'profession': {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

# Updated dictionary after modification: {'name': 'Alice', 'age': 40, 'city': 'New York', 'profession': 'Doctor'}

# City: New York

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

my_dict['Profession'] = "Doctor"

print(f"after adding doctor {my_dict}")

my_dict["age"] = 40

print(f"age modify {my_dict}")

city = my_dict["city"]

print(f"city {city}")

