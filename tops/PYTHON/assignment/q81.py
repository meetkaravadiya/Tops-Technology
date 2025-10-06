# Write a Python program to write a list to a file.

list = ["meet","param","shubh","ronit","tanisha"]

f = open('81.txt','w')

for i in list:
    f.write(i + "\n")

f.close()