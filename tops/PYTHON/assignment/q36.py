# Write a Python function that takes a list and returns a new list with
# unique elements of the first list. 

l1 = [1,2,4,6,8,9,10,9,2,6]

l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)