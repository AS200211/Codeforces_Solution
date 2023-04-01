for _ in range(int(input())):
    n=int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] < b[n - i - 1]:
            a[i],b[n-i-1] = b[n - i - 1],a[i]
        else:
            break
    print(max(a)*max(b))