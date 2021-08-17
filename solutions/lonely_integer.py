def lonelyinteger(a):
    a.sort()
    
    if len(a) == 1: return a[0]
    if len(a) == 3:
        if a[0] == a[1]: return a[2]
        if a[0] == a[2]: return a[1]
        return a[0]
    if a[0] != a[1]: return a[0]

    prev = False
    for i in range(1, len(a) - 1):
        if a[i] != a[i + 1]:
            if prev == True: return a[i]
            prev = True
        else: prev = False
    return a[len(a) - 1]