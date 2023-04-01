for _ in range(int(input())):
    a,b = map(int,input().split())
    c = -1
    f = []
    for i in range(a,b+1):
        d = list(str(i))
        d.sort()
        e = abs(int(d[len(d)-1])-int(d[0]))
        f.append(e)
    g = -1
    y = max(f)
    if f.count(y)>1:
        for i in range(len(f)-1,-1,-1):
            if f[i]==y:
                g = i
                break


    if g==-1:
        x = f.index(max(f))
    else:
        x=g
    print(a+x)