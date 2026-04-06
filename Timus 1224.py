n, m = map(int, input().split())
print((2 *(n - 1) * (n <= m)) + ((2 *(m - 1) + 1) * (n > m)))
