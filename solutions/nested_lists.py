def nested_lists():
    arr = []
    second_lowest_names = []
    scores = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        scores.add(score)
        
    second_lowest = sorted(scores)[1]

    for name, score in arr:
        if score == second_lowest:
            second_lowest_names.append(name)

    for name in sorted(second_lowest_names):
        print(name, end='\n')