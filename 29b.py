for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==1:
        print(0)
    else:
        s=0
        d = []
        for i in range(a):
            b.append(list(map(int,input().split())))
        for i in d:
            x = i
            for j in 