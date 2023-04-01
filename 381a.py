n = int(input())
arr = list(map(int,input().split()))
j = n-1
i = 0
k = 0
pa = 0
pb = 0
while i<=j:
    if arr[i]>=arr[j]:
        m = arr[i]
        i+=1
    else:
        m = arr[j]
        j-=1
    if k%2==0:
        pa+=m
    else:
        pb+=m
    k+=1
print(pa,pb)
    