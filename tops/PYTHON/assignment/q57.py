# Write a Python program to find the highest 3 values in a dictionary

a = {'a': 50, 'b': 20, 'c': 90, 'd': 40, 'e': 70}

top = sorted(a.values(), reverse=True)[:3]

print(top)
