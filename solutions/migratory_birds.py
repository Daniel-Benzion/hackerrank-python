def migratory_birds(arr):
    
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0

    

    for bird in arr: 
        
        if bird == 1: one += 1
        elif bird == 2: two += 1
        elif bird == 3: three += 1
        elif bird == 4: four += 1
        else: five += 1
            

    if one >= two and one >= three and one >= four and one >= five: return 1
    if two >= three and two >= four and two >= five: return 2
    if three >= four and three >= five: return 3
    if four >=  five: return 4
    return 5