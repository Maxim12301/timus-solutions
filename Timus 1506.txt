n, k = map(int, input().split())
num_list = list(input().split())

for i in range(n):    
    num_list[i] = ' ' * (4 - len(num_list[i])) + num_list[i]

num_clm = ((n // k) + 1 * ((n // k) < (n / k))) 

for i in range(num_clm):
    for j in range(k):
        print(num_list[(i + num_clm * j) * ((i + num_clm * j) < n)] * ((i + num_clm * j) < n) , end='')
    print('')
