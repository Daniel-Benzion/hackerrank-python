def drawing_book(n, p):
    
    total_front = n // 2
    target_front = p // 2

    back = total_front - target_front

    return min(target_front, back)