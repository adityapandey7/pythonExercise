# Count all letters, digits, and special symbols from a given string
# Given:

# str1 = "P@#yn26at^&i5ve"
# Expected Outcome:

# Total counts of chars, digits, and symbols 

# Chars = 8 
# Digits = 3 
# Symbol = 4

str = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbol = 0

for ch in str:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        chars += 1
    else:
        symbol += 1

print(f' chars: {chars} digits {digits} sysmbol {symbol}')
