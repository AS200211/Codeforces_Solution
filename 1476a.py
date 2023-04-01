for _ in range(int(input())):
    n,k = map(int,input().split())
    c = (n+k-1)//k
    k*=c
    print((k+n-1)//n)