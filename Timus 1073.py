def res(n):
    if n in s:
        return 1
    
    for i in range(0, int(n ** .5)+ 1):
        for j in range(1, int(n ** .5)+ 1):
            for z in range(1, int(n ** .5)+ 1):
                if i ** 2 + j ** 2 + z ** 2 == n:
                    return 3 - 1 * (i == 0)
    return 4
        

num = int(input())
s = set([i ** 2 for i in range(1, 246)])
ans = res(num)

print(ans)
