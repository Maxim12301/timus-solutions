n = int(input())
l_n = list(input().split()) + [11]

c = 1
ans = ''

for i in range(n):
    if l_n[i] == l_n[i + 1]:
        c += 1
    else:
        ans += str(c) + ' ' + str(l_n[i]) + ' '
        c = 1


print(ans)
