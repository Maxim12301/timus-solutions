n = int(input())
guests = 2

for i in range(n):
    
    guests += 1
    guest = input()
    
    if '+one' in guest:
        
        guests += 1

if guests == 13:
    
    print((guests * 100) + 100)

else:
    
    print(guests * 100)
