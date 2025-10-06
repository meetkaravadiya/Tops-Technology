# Write a Python script to check if a given key already exists in a
# dictionary. 

dic = {"cod":1500,
       "god of war": 2000,
       "super mario": 1000
       }

ckey = 1000

if ckey in dic.keys():
    print("key exists in dictionary ")
else:
    print("key not exists")