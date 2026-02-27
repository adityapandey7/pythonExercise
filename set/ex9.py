# Write a code to count the number of unique words in the given a sentence.

# Given:

# sentence = "dog is a simple animal dogs is selfless animal"
# Expected Output:

# Number of unique words: 7

sentence = "dog is a simple animal dogs is selfless animal"
list1 = sentence.lower().split(" ")
set1 = set(list1)

print(f"list {list1} and unique word {set1} total unique word {len(set1)}")