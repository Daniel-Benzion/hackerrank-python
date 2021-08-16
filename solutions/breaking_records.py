def breaking_records(scores):
    min = scores[0]
    max = scores[0]
    count = [0, 0]
    
    for i in range(1, len(scores)):
        if scores[i] > max: 
            count[0] += 1
            max = scores[i]
        elif scores[i] < min: 
            count[1] += 1
            min = scores[i]
    return count