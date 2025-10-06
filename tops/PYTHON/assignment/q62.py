# Write a Python function to check whether a number is in a given range

def check(num):

    if 10 < num < 20:
        return "number is in range"
    else:
        return "number is not in range"

num = int(input("enter the number"))

print(check(num))
