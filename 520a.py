n = int(input())
s = input()
s = s.lower()
s = set(list(s))
if len(s)==26:
    print("YES")
else:
    print("NO")