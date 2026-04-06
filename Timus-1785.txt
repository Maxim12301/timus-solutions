num = int(input())

if num in range(1, 5):
    print('few')
elif num in range(5, 10):
    print('several')
elif num in range(10, 20):
    print('pack')
elif num in range(20, 50):
    print('lots')
elif num in range(50, 100):
    print('horde')
elif num in range(100, 250):
    print('throng')
elif num in range(250, 500):
    print('swarm')
elif num in range(500, 1000):
    print('zounds')
else:
    print('legion')
