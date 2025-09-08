# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string. 

str = input("enter the syring: ")

if len(str)>2:
    str = str[:2]+str[-2:]
    print(str)
else:
    print("")
