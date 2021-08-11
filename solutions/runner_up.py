def runner_up(arr):
    max_num = max(arr)
    arr.sort()
    arr.reverse()
    for i in range(0, len(arr)):
        if arr[i] != max_num:
            print(arr[i])
            break