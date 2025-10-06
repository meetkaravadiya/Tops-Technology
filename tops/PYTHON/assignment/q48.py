# Write a Python script to sort (ascending and descending) a
# dictionary by value. 

dic = {"cod":1500,
       "god of war": 2000,
       "super mario": 1000
       }

print("dictnory: ",dic)

ace = dict(sorted(dic.items(), key = lambda x: x[1]))
print("ascending: ",ace)

dace = dict(sorted(dic.items(), key = lambda x: x[1], reverse=True))
print("descending: ",dace)