# Write a Python program to check whether a list contains a sub list

l1 = [1,2,3,4,5,6,7,8]

l2 = [4,5]
s = False
for i in range(len(l1)-len(l2)+1):
    if l1[i:i+len(l2)] == l2:
        s = True
        break

print(s)