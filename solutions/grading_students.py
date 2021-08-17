def grading_students(grades):
    for i in range(0, len(grades)):
        if grades[i] < 38: continue
        sub = grades[i] % 10
        if sub in (3, 4):
            grades[i] = ((grades[i] // 10) * 10) + 5
        if sub in (8, 9):
            grades[i] = ((grades[i] // 10) * 10) + 10
    return grades