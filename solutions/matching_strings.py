def matchingStrings(strings, queries):
    arr = []
    for i in range (0, len(queries)): arr.append(strings.count(queries[i]))
    return arr