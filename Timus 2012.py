f = int(input())
task = 12 - f # оставшиеся задачи
time = task * 45 # время на решение оставшихся задач

if 240 - time >= 0:
    print('YES')
else:
    print('NO')
    
