# Write a program to find all occurrences of “USA” in a given string ignoring the case.

# Given:

# str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Outcome:

# The USA count is: 2

Str1 = "Welcome to USA. usa awesome, isn't it?"

occurences = Str1.lower().count('usa')

print(f"occurences of USA {occurences}")