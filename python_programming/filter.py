ages = [5, 12, 17, 18, 24, 32 ]

def legal_age(x): 
    if x < 18:  
        return False
    else: 
        return True

print(list(filter(legal_age, ages)))

    
