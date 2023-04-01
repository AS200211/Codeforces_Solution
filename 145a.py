def sol():
    s = input()
    m = {}

    for i in s:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    
    ans = 4
    x = len(m)
    
    if x == 4 or x == 3:
        ans = 4
    elif x == 1:
        ans = -1
    else:
        if m[s[0]] == 1 or m[s[1]] == 1 or m[s[2]] == 1 or m[s[3]] == 1:
            ans = 6
        else:
            ans = 4
    
    print(ans)

t = int(input())

for _ in range(t):
    sol()
