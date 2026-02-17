# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

# Given:

# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:

# AzbycX

def mix_strings(str1,str2):
    i,j = 0, len(str2)-1
    s3 = ""

    while i<len(str1) and j>=0:
        s3 += str1[i]+str2[j]
        i+=1
        j-=1
    
    if i<len(str1):
        s3 += str1[i:]
    
    if j>=0:
        s3 += str2[j::-1]
    
    return s3

print(mix_strings("abc", "xyz78"))
