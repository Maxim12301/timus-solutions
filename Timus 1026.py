n = int(input())
numbers = []

for j in range(n):

    numbers.append(int(input()))

numbers.sort()

a = input()
k = int(input())

for z in range(k):

    print(numbers[int(input()) - 1])
