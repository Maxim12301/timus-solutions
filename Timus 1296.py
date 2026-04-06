n = int(input())

num_list = []
res = set([0])

for i in range(n):
    num_list.append(int(input()))

m = 0

for j in num_list:
    if j >= 0:
        m += j
    elif m + j <= 0:
        res.add(m)
        m = 0
    else:
        res.add(m)
        m += j
res.add(m)

print(max(res))
        
