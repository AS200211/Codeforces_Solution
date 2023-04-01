t = int(input())

for _ in range(t):
    n, k = map(int, input().split())


    a = [-i for i in range(1, n)]
    a.append(n * (n - 1) // 2 - sum(a))


    for i in range(2, n + 1):
        for j in range(n - i + 1):
            subarray = a[j:j+i]
            if sum(subarray) < 0:
                a[j+i-1] *= -1
                k -= 1
                if k == 0:
                    break
        if k == 0:
            break
    else:
        a[-1] *= -1

    print(*a)