def ginortS(n):
    m, u, o, e = [], [], [], []
    for i in sorted(n):
        if i.isalpha():
            x = u if i.isupper() else m
        else:
            x = o if int(i) % 2 else e
        x.append(i)
    print("".join(m + u + o + e))