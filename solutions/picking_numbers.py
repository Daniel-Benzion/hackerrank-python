def picking_numbers(a):
    
    a.sort()
    current_size = 0
    result = 0
    
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[j] - a[i] <= 1: current_size += 1
            else: break
            
        if current_size > result: result = current_size
        current_size = 0
    
    return result