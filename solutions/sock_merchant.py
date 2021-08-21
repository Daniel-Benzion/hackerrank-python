def sock_merchant(n, ar):
    
    pairs = {}
    for sock in ar:
        try:
            pairs[sock] += 1
        except:
            pairs[sock] = 1
            
    return sum([p // 2 for p in pairs.values()])