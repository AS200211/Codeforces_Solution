for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if b<=d and c<=a+d-b:
        print((d-b)+(a+d-b-c))
    else:
        print(-1)