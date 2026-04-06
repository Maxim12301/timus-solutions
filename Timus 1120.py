
s = int(input())
if s & (s - 1) == 0:
    
    print(s, 1)
    
else:
    for n in range(int((2 * s) ** .5) + 4, 1, -1):
        a = (2 * s - n ** 2 - n) / (2 * n)
        if (a + 1) > 0 and a == int(a):
            print(int(a) + 1, n)
            break
    
