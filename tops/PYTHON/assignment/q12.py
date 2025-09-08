# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("enter the 1st number: "))
b = int(input("enter the 2nd number: "))
c = int(input("enter the 3rd number: "))

if a == b or b == c or a == c:
    sum = 0
else:
    sum = a + b + c

print("sum is ", sum)