# Write a python program to find the longest words. 

f = open("72.txt", 'r')

words = f.read().split()  
max_len = len(max(words, key=len))  


longest_words = [word for word in words if len(word) == max_len]

print("Longest word(s):", longest_words)


