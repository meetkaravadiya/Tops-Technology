# Write a Python program to unzip a list of tuples into individual lists. 

my = [(1,23),("meet","game"),(99,20)]

num,char = zip(*my)

print(list(num))
print(list(char))