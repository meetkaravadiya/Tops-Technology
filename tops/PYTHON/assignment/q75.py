# Write a Python program to read last n lines of a file. 

f = open("74.txt",'r')

num = 3 
line = f.readlines()

for i in line[-num:]:
    print(i)


