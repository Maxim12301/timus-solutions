def num_div(num):
    div_list = []
    while n > 1:
        
        for div in range(9, 2, -1):
            
            if num % div == 0:
                num //= div
                div_list.append(div)
                break
        
        else:
            
            if num >= 10:
                return -1
            
            elif num > 1:
                div_list.append(num)
                break
            
            else:
                break
            
    return div_list


def min_q(num):
    q = ''
    num_list = num_div(num)
    if num_list == -1:
        return -1
    
    elif num == 1:
        return 1
    
    elif num == 0:
        return 10
    
    else:
        num_list.sort()
        num_list = list(map(str, num_list))
        for i in num_list:
            q += i
        return q


n = int(input())
print(min_q(n))
