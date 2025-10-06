# Write a Python program to count the number of lines in a text file. 

f = open("74.txt", 'r')

count = 0
for line in f:
    count += 1

print(count)
