y = int(input())
a = list(map(int,input().split()))
b = a.count(1)
if b>0:
    print("HARD")
else:
    print("EASY")