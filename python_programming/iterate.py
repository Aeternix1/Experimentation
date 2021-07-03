# Simple list comprehension
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares) 
 
# Equavalent operation using for loops
cubes = []
for x in [1, 2, 3, 4, 5]:
    cubes.append(x ** 3)
print(cubes)

# Equivalent operation using map function 
def square(x): 
    return x ** 2 

values = [1, 2, 3, 4, 5]
print(list(map(square, values)))

