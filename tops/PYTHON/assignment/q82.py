# Write a Python program to copy the contents of a file to another file.
f1 = open('81.txt','r')
f2 = open('82.txt','w')

for i in f1:
    f2.write(i)

f2.close()