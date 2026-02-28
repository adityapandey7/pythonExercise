# n Python, we can initialize the keys with the same values.

# Given:

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# Expected output:

# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict1 = {}

for item in employees:
    dict1.update({item:defaults})

print(dict1)
