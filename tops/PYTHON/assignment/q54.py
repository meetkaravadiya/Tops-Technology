# Write a Python program to check multiple keys exists in a dictionary 

dic = {"cod":1500,
       "god of war": 2000,
       "super mario": 1000
       }

ckey = ["cod", "god of war","meet"]

check = True

for i in ckey:
    if i not in dic.keys():
        check = False
        break

if check:
    print(True)
else:
    print(False)
