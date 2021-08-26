def symmetric_difference(arr):
    a,b = [set(arr.split()) for _ in range(4)][1::2]
    print(*sorted(a^b, key=int), sep='\n')