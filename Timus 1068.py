n = int(input())

if n >= 1:
    print(sum([i for i in range(1, n + 1)]))
else:
    print(sum([i for i in range(n, 2)]))
    
