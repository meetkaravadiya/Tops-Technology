# Write a Python program to remove duplicates from a list.

l1=[]
for i in range(5):
    n = input("enter the elements: ")
    l1.append(n)

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)

print("orignal: ",l1)
print("remove duplicates: ",l2)