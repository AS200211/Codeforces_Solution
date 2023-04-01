n = int(input())
a = [4,7,47,74,44,444,447,474,477,777,774,744]
c = 0
for i in a:
    if n%i==0:
        c+=1
if c>0:
    print("YES")
else:
    print("NO")