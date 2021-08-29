def set_difference(arr1, arr2):
    set_1 = set(map(int, arr1.split()))
    set_2 = set(map(int, arr2.split()))
    print(len(set_1 - set_2))