def closest_numbers(arr):
    
    arr.sort()
    hMap = {}
    low = arr[1] - arr[0]
    
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < low: low = diff
        if hMap.get(diff):
            hMap[diff] = [*hMap.get(diff), arr[i], arr[i + 1]]
        else:
            hMap[diff] = [arr[i], arr[i + 1]]
            
    return hMap.get(low)