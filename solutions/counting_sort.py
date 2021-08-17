def counting_sort(arr):
    freq = [0 for _ in range(100)]
    for i in range(0, len(arr)): freq[arr[i]] += 1
    return freq