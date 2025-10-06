# )Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string. 

str = "meet"

d = {}

for i in str:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1

print(d)