# Write a Python function to calculate the factorial of a number (a
# nonnegative integer) 

def fact(num):
    fact = 1

    for i in range(1,num+1):
        fact *= i
    
    return fact

num = int(input("enter the number: "))

print(fact(num))

