# Check if all items in the tuple are the same
# tuple1 = (45, 45, 45, 45)

tuple1 = (45, 45, 45, 45)

flag = True

for item in tuple1:
    if item == tuple1[0]:
        pass
    else:
        flag = False

if flag:
    print("true")
else:
    print("false")