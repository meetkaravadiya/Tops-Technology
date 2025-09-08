#  Write a Python program to count the occurrences of each word in a given sentence.

text = input("enter the text: ")
textsp = text.split()
word = []

for i in textsp:
    if i not in word:
        word.append(i)
        count = 0
        for j in textsp:
            if i == j:
                count+=1
        print(f"{i} = {count}")


