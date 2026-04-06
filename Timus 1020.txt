n, r = map(float, input().split())

n = int(n)

l = 2 * 3.14 * r
start_x, start_y = map(float, input().split())
o_x, o_y = start_x, start_y

if n == 1:
    print(round(l, 2))
else:
    for i in range(n - 1):
        n_x, n_y = map(float, input().split())
        l += (((n_x - o_x) ** 2) + ((n_y - o_y) ** 2)) ** .5
        o_x, o_y = n_x, n_y
    else:
        n_x, n_y  = start_x, start_y
        l += (((n_x - o_x) ** 2) + ((n_y - o_y) ** 2)) ** .5
    print(round(l, 2))
