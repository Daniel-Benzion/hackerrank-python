def no_idea(m, n, arr, A, B):
    print(sum([(i in A) - (i in B) for i in arr]))