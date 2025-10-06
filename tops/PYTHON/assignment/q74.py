# Write a Python program to read first n lines of a file. 

f = open("74.txt",'r')

num = 3 

for i in range(num):
    line = f.readline()
    print(line)

