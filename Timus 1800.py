l, h, v = map(int, input().split())
h /= 100
l /= 100
v /= 60
if (l >= 2 * h):
    print('butter')
else:
    t = (((2 * h) - l) / 9.81) ** .5
    n = v * t
    n %= 1
    if  n < .25 or n > .75: 
        print('butter')
    else:
        print('bread')
