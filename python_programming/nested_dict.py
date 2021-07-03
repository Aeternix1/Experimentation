# Storing multiple types of data in a dictionary 
jane = {'name': {"fname": "Jane", "lname": "Doe"},
        'jobs': ['dev', 'manager'],
        'age': 40.5}

print(jane['name']['fname']) 
print(jane['jobs'][1]) 

jane['jobs'].append('data entry')

print(jane['jobs'])
