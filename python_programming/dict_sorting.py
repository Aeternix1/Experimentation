D = {'a': 1 , 'b': 2, 'c': 3}
print(D) 

#What should we do if we want to print the keys:value pairs in order? 
for key in sorted(D): 
    print(key, "=>", D[key])
