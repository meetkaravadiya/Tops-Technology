# Write python program that swap two number with temp variable
# and without temp variable

num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
a = num1
b = num2
# with temp variable
temp = num1
num1 = num2
num2 = temp
print(f"now no1 is {num1}")
print(f"now no2 is {num2}")
print("--------------------------------------------")
print("this swap is done without temp variable")

# without temp variable

a = a + b
b = a - b
a = a - b
print(f"now no1 is {a}")
print(f"now no2 is {b}")