for _ in range(int(input())):
    a,b = map(int,input().split())
    c = 0
    if a%b==0:
        print(c)
    else:
        print(b-a%b)