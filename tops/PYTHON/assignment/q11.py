#  Write a Python program to test whether a passed letter is a vowel or not. 

letter = input("enter the letter: ")

vowel = "aeiouAEIOU"

if letter in vowel:
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is not a vowel")