# Practicing the use of Tuples 

T = (1, 2, 3, 4) 
print(len(T))
print(T)

# Concatenating a Tuple 
T = T + (5, 6)    
print(T) 

T = T + (5,)
print(T)

# Can conduct indexing and slicing operations
print('Print T[2] = ' + str(T[2]))
print('Print T[-1] = ' + str(T[-1]))

# Tuple specific functions
print("The amount of '5s' in this tuple is " + str(T.count(5))) 
print("The value 5 is at index: " + str(T.index(5))) 
print(type(T.index(5)))

# Can't create new values but you can create a new tuple 
T = (2,) + T[1:]
print(T)
# T[0] = 5    # Error


T = 'spam', 3.0, [11, 22, 33]
print(T[1])
print(T[2][1])
T.append(4) # Error





