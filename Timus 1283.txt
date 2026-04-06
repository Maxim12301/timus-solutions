gold, min_gold, percent = map(int, input().split())
year = 0

if gold > min_gold:
    
    while gold > min_gold:
    
        year += 1
        gold = ((100 - percent) / 100) * gold
        
    print(year)    

else:

    print(0)


