# Write a Python program to append text to a file and display the text. 

f = open('72.txt','a')

f.write("\n hello this is add")

f.close()

f = open('72.txt','r')
line = f.read()
print(line)