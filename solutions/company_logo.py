from collections import Counter

def company_logo():
    chars = Counter(input()).items()

    for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
        print(char, n)