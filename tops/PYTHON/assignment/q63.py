# Write a Python function to check whether a number is perfect or not. 

def perfect(num):
    div = 0
    for i in range(1,num):
        if num % i == 0:
            div += i
        
    return div == num

num = int(input("enter the number: "))

if perfect(num):
    print("perfect number")
else:
    print("not perfect number")
    