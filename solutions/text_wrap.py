def text_wrap(string, max_width):
    i = 0
    arr = []
    while True:
        if i + max_width > len(string): break
        arr.append(string[i:i + max_width])
        i += max_width
    
    arr.append(string[i:])
    return "\n".join(word for word in arr)