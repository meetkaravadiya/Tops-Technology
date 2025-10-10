# Write a Python program to check whether a list contains a sub list

l1 = [23,45,99,100,101,44,58]

l2 = [45,58]

count = 0
for i in l2:
    if i in l1:
        count +=1

if count == len(l2):
    print(True)
else:
    print(False)