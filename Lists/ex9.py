# Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = []

for i in range(len(list1)):
    for j in range(len(list2)):
        result.append(list1[i] + list2[j])


print(f"new list: {result}")