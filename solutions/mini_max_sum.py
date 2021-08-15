def mini_max_sum(arr):

    one = sum(arr[1:])
    two = sum(arr[2:], arr[0])
    three = sum(arr[3:], sum(arr[0:2]))
    four = sum(arr[0:3], arr[4])
    five = sum(arr[0:4])

    sum_arr = [one, two, three, four, five]
    
    print(min(sum_arr), max(sum_arr), sep=" ")