for i in range(int(input())):
    n,q=map(int,input().split())
    m=0
    x=[m:=(int(i)+m) for i in input().split()]
    x.append(0)
    for i in range(q):
         l,r,k=map(int,input().split())
         if (k*(r-l+1)+(x[n-1]-x[r-1])+(x[l-2]))&1:
             print("YES")
         else:
             print("NO")