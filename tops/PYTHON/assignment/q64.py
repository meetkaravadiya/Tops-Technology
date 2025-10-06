# Write a Python function that checks whether a passed string is
# palindrome or not 

def palin(str):

    str = str.replace(" ","").lower()

    return str == str[::-1]

text = input("enter the word:")

if palin(text):
    print("palindrome")
else:
    print("not palindrome")