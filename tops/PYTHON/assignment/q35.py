# Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30.

l1=[]

for i in range(1,31):
    s= i**2
    l1.append(s)

first = l1[:5]
last = l1[-5:]

print("first 5 elements are: ",first)
print("last 5 elements are: ",last) 