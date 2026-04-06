n, m = map(int, input().split())
l_n = [i for i in range(n + 1)]
ans = []

for i in range(m):
    a = input()
    if 'L' in a:
        ans.append(l_n[int(a[1:])])
    if 'D' in a:
        l_n.pop(int(a[1:]))

for j in range(len(ans)):
    print(ans[j])
