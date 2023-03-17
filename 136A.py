n = int(input())
ar = list(map(int,input().split()))
a = [-1]*n
for i in range(n):
    a[i]=ar.index(i+1)+1
print(*a)