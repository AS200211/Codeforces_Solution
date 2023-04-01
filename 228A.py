s = list(map(int,input().split()))
if len(s)==len(set(s)):
    print(0)
else:
    print(len(s)-len(set(s)))