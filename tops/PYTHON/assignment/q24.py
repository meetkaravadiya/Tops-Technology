# Write a Python function to insert a string in the middle of a string.

str = input("enter the string: ")
mid = input("enter the mid string: ")

pos = len(str)//2

str = str[:pos] + mid + str[pos:]

print(str)