n, x = map(int, input().split())

left_board = -10000
right_board = 10000
l_num = list(map(int, input().split()))

for num in l_num:

    if num > 0:
        
        right_board = min(right_board, num)
    
    if num < 0:
        
        left_board = max(left_board, num)
    
if (x > 0 and right_board < x) or (x < 0 and left_board > x):
    
    print('Impossible')

else:
    
    if x > 0:
        
        print(x, x + 2 * abs(left_board))
        
    if x < 0:
        
        print(abs(x) + 2 * right_board, abs(x))
