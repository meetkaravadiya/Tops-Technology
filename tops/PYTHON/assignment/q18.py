# Write a Python program to count occurrences of a substring in a string. 

text = input("enter the text: ")
sub = input("enter the substring: ")
count = 0
lenght = len(sub)

for i in range(len(text)- lenght + 1):
    if text[i:i+lenght] == sub:
        count+=1

print(f"{sub} is occurs {count} in the string")