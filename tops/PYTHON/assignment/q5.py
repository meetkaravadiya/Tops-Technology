# Write a Python program to get the Factorial number of given numbers. 

num = int(input("enter the number: "))
fact = 1
for i in range(1,num+1):
    fact*= i

print(f"factorial of {num} is {fact}")
