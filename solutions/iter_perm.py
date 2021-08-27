from itertools import permutations

def iter_perm(s, k):
    print(*["".join(i) for i in permutations(sorted(s), int(k))], sep='\n')
    