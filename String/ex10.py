# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

# Given:

# str1 = "PYnative29@#8496"
# Expected Outcome:

# Sum is: 38 Average is  6.333333333333333

str1 = "PYnative29@#8496"
digit = 0
i=0

for ch in str1:
    if ch.isdigit():
        digit += int(ch)
        i += 1

print(f"sum is {digit} avg is {digit/i}")
