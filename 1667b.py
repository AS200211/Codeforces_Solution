for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    a = min(arr)
    c = 0
    for i in arr:
        c+=i-a
    print(c)