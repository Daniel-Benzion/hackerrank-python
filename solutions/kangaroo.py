def kangaroo(x1, v1, x2, v2):
    
    if x1 == x2 and v1 == v2: return "YES"
    if v1 == v2 and x1 != x2: return "NO"

    if (v2 > v1 and x2 < x1) or (v1 > v2 and x1 < x2):
        if (x1 - x2) % (v2 - v1) == 0 or (x2 - x1) % (v1 - v2) == 0: 
            return "YES"


    return "NO"