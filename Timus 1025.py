def BubbleSort(num_list):
    
    len_num_list = len(num_list)
    
    for i in range(len_num_list):
        
        for z in range(len_num_list - 1):
            
            if num_list[z] > num_list[z + 1]:
                
                num_list[z], num_list[z + 1] = num_list[z + 1], num_list[z]
                
    return num_list
        

k = int(input())
group_list = list(map(int, input().split()))
group_list = BubbleSort(group_list)
amount_voter = 0

for j in range((len(group_list) // 2) + 1):

    amount_voter += (group_list[j] // 2) + 1

print(amount_voter)
