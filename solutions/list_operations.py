def list_operations():
    N = int(input())
    arr = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "(" + ",".join(args) + ")"
            eval("arr." + cmd)
        else:
            print(arr)