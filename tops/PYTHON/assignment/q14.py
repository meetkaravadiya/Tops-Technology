# Write a python program to sum of the first n positive integers. 

a = int(input("enter the positive number: "))
sum = 0

if a > 0:
    for i in range(1,a+1):
        sum += i
    print(f"sum of first {a} positive integer is {sum}")
else:
    print(f"please enter the positive number")
    