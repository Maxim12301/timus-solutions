k, n = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
    ans = ans + a[i]
    ans -= k
    if ans <= 0:
        ans = 0


print(ans)
