def rotate_left(d, arr):
    if len(arr) == d: return arr
    if len(arr) < d: d = d % len(arr)
        
    for _ in range(d): arr = [*arr[1:], arr[0]]
        
    return arr