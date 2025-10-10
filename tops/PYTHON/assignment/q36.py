# Write a Python function that takes a list and returns a new list with
# unique elements of the first list. 

l1= [10,20,20,"java","python",45]

l2 = []

for i in l1:
    if l1.count(i) == 1:
        l2.append(i)

print(l2)