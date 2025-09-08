# Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string. 

text1 = input("enter the 1st text: ")
text2 = input("enter the 2nd text: ")

str1 = text2[:2] + text1[2:]
str2 = text1[:2] + text2[2:]

print(str1 + " " + str2)
