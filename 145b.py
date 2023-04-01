import math

def solve(n):
    return int(math.sqrt(n - 1))
 
t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))