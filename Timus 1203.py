n = int(input())
conf_list = []
ans = 0
time = 0

for i in range(n):
    line = list(map(int, input().split()))
    conf_list.append(line[::-1])

conf_list.sort()

for i in range(n):
    if conf_list[i][1] - time >= 1:
        ans += 1
        time = conf_list[i][0]
        
print(ans)
