# Write a Python function to get the largest number, smallest num and sum of all from a list. 
l1 = []
for i in range(5):
    n = int(input("enter the number: "))
    l1.append(n)

max_num = max(l1)
min_num = min(l1)
sum_num = sum(l1)

print(l1)
print(f"largest number is {max_num}.")
print(f"smallest number is {min_num}.")
print(f"sum of list is {sum_num}.")