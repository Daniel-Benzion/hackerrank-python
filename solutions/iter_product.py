from itertools import product

def iter_product(a, b):
    x = list(map(int, a.split()))
    y = list(map(int, b.split()))
    print(*product(x, y))