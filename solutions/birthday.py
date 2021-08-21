def birthday(s, d, m):

    correct = 0
    total = 0
    
    for i in range(0, len(s)):
        
        total = s[i]
        
        for j in range(i + 1, i + m):
            if j >= len(s): break
            total += s[j]
           
        if total == d:
            correct += 1
    
    return correct