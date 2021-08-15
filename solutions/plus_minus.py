def plus_minus(arr):
    div = len(arr)
    neg = 0
    pos = 0
    zer = 0
    for num in arr:
        if num < 0: neg += 1
        elif num > 0: pos += 1
        else: zer += 1
    print(round(pos / div, 6))
    print(round(neg / div, 6))
    print(round(zer / div, 6))