for _ in range(int(input())):
    n = int(input())
    a = input()
    a = a.lower()
    a = set(list(a))
    
    if len(a)==4 and {'m','e','o','w'}==a:
        
        print("YES")
    else:
        print("NO")
    