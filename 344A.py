n = int(input())
a = []
for i in range(n):
    a.append(input())
    
c = 1
for i in range(1,n):
    if a[i-1]==a[i]:
        pass
    else:
        c+=1
print(c)