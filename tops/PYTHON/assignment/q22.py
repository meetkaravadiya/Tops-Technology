#  Write a Python function to reverses a string if its length is a multiple of 4.

str = input("enter the string: ")

if len(str)%4 == 0:
    print(str[::-1])
else:
    print(str)

