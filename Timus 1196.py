import sys


tut_list = set()

for i in range(int(sys.stdin.readline())):
    
    tut_list.add(sys.stdin.readline())



ans = 0

for i in range(int(sys.stdin.readline())):  
    
    ans += 1 * (sys.stdin.readline() in tut_list)
    

print(ans)
