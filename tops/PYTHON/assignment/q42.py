# Write a Python program to split a list into different variables. 

l1 = ["meet", "param", "ronit", "shubh"]

var = 97 

for i in l1:
    ch = chr(var)  
    ch = i 
    print(f"{chr(var)} = {ch}")
    var += 1  

