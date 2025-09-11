# Write a Python function that takes two lists and returns true if they
# have at least one common member. 

l1 = [23,45,67,89,20]
l2 = [2,3,4,5,78,89]

for i in l1:
    if i in l2:
        print(True)

