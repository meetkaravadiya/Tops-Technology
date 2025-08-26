# Write a Python program to get the Fibonacci series of given range.

num = int(input("enter the range "))
a = 0
b = 1
c = 0

for i in range(num):
        c = a + b
        print(c, end=" ")
        a, b = b, c
