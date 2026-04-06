n, k = map(int, input().split())
print((((2 * n // k) + 1 * ((2 * n // k) != (2 * n / k))) * (n > k)) + (2 * (n <= k)))

