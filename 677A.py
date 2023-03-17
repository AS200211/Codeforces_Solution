n,h = map(int,input().split())
arr = list(map(int,input().split()))
c = 0
for i in arr:
    if i>h:
        c+=2
    else:
        c+=1
print(c)