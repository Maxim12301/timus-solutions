def InsertionSort(item_list, item):
    len_item_list = len(item_list)
    
    for i in range(len_item_list):
        
        if item_list[i] == item:
            
            item_list.insert(i, item)
            return item_list
        
    item_list.append(item)
    return item_list


n = int(input())
regions = []
unique_region = set()
max_amount = 0

for j in range(2 ** n):
    
    name, region = input().split()
    unique_region.add(region)
    regions = InsertionSort(regions, region)
    
for y in list(unique_region):
    
    max_amount = max(max_amount, regions.count(y))

ans = 0
if max_amount > 1:
    
    ans -= 1 * (max_amount & (max_amount - 1) == 0)
    
    while max_amount != 0:
        
        max_amount = max_amount // 2
        ans += 1
    
if ans >= n:
    
    print(0)

else:
    
    print(n - ans)


