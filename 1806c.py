for _ in range(int(input())):
    n = int(input())
    s = input()
    ma = 200007
    mod = 1000000007
    mp = [-1]*26
    f = 0
    for i in range(n):
        curr = ord(s[i])-ord('a')
        if mp[curr]==-1:
            mp[curr]=i%2
        else:
            if mp[curr]!=(i%2):
                # print("NO")
                f = 1
    if f==0:
        print("YES")
    else:
        print("NO")
    
                
    