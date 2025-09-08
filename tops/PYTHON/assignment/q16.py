# Write a Python program to count the number of characters (character frequency) in a string 

str1 = input("enter the string: ")
a = []
for i in str1:
    if i in a:
        continue
    else:
       a.append(i)
       count = 0
       for j in str1:
            if i == j:
                count += 1 
       print(f"{i} = {count}")
     