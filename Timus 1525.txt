size = list(map(int, input().split()))
line = input()
line_x = ''
line_y = ''
line_z = ''

for i in line:
    if i in 'fb':
        line_x += i
    
    if i in 'lr':
        line_y += i
    
    if i in 'ud':
        line_z += i

max_x = 0
min_x = 0
max_y = 0
min_y = 0
max_z = 0
min_z = 0
dif = []

for i in line_x:
    if i == 'f':
        max_x += (max_x < 0)
        min_x += 1
    
    if i == 'b':
        min_x -= (min_x > 0)
        max_x -= 1

dif.append(max_x - min_x)



for i in line_y:
    if i == 'l':
        max_y += (max_y < 0)
        min_y += 1
    
    if i == 'r':
        min_y -= (min_y > 0)
        max_y -= 1

dif.append(max_y - min_y)


for i in line_z:
    if i == 'u':
        max_z += (max_z < 0)
        min_z += 1
    
    if i == 'd':
        min_z -= (min_z > 0)
        max_z -= 1

dif.append(max_z - min_z)


x = size[2] + dif[0]
y = size[0] + dif[1]
z = size[1] + dif[2]

if x <= 0:
    x = 1

if y <= 0:
    y = 1
    
if z <= 0:
    z = 1

print(x * y * z)
