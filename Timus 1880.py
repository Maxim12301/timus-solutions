def SelectionSort(num_list):
    new_num_list = []
    len_num_list = len(num_list)
    
    for i in range(len_num_list):
        
        min_num = min(num_list)
        num_list.remove(min_num)
        new_num_list.append(min_num)
        
    return new_num_list


ans = 0

n = int(input())
num = list(input().split())
s = set(x for x in num)
d = dict.fromkeys(s, 1)

n = int(input())
num = SelectionSort(list(input().split()))

for i in range(n):
    
    if num[i] in s:
        
        d[num[i]] += 1

        
n = int(input())
num = list(input().split())

for i in range(n):
    
    if num[i] in s:
        
        d[num[i]] += 1

num = SelectionSort(list(d.values()))

for i in num[::-1]:
    
    if i != 3:
        
        break
    
    ans += 1

print(ans)

