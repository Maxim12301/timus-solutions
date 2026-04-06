def min_score(n_list):
    score_min = sum(n_list)
    if n_list[9] > 20 and n_list[8] == 10:
        score_min += 10
    return score_min


def max_score(n_list):
    score_max = sum(n_list)
    
    for i in range(7):
        
        if n_list[i] == 10:
            score_max += n_list[i + 1]
            
            if n_list[i + 1] == 10:
                score_max += n_list[i + 2]
    
    if n_list[7] == 10:
        score_max += n_list[8]
    
    if n_list[7] == 10 and n_list[8] == 10:
        score_max += 10 * (n_list[9] >= 10) + n_list[9] * (n_list[9] < 10)
    
    if n_list[8] == 10 and (n_list[9] <= 20):
        score_max += n_list[9]
    
    if n_list[8] == 10 and (n_list[9] > 20):
        score_max += 20
            
    return score_max
    
    

num_list = list(map(int,input().split())) + [0, 0]
print(min_score(num_list), max_score(num_list))
