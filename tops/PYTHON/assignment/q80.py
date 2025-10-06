# Write a Python program to count the frequency of words in a file.

f = open("72.txt", 'r')

words = f.read().split() 
d = {}
for i in words:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1

print(d)