def find_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    total_scores = sum(query_scores)
    result = "{:.2f}".format(total_scores / 3)
    print(result)