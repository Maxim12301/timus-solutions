n, a, b = map(int, input().split())
x, y = [1] * (n + 1), [1] * (n + 1)


for i in range(2, n + 1):
    x[i] = (y[i - 1] + x[i - 1] - y[i - a - 1] * (i - a > 0)) % (10 ** 9 + 7)
    y[i] = (x[i - 1] + y[i - 1] - x[i - b - 1] * (i - b > 0)) % (10 ** 9 + 7)

print((x[n] + y[n]) % (10 ** 9 + 7))
