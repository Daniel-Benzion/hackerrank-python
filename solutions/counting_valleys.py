def counting_valleys(steps, path):
    level = 0
    count = 0

    for i in range(0, steps):
        if path[i] == "D": level -= 1
        else:
            level += 1
            if level == 0: count += 1
    return count
