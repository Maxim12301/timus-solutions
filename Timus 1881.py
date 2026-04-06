h, w, n = map(int, input().split())
amount_line = 1
amount_sym = 0

for i in range(n):
    line = input()
    amount_sym += len(line)
    if amount_sym > w:
        amount_sym = len(line)
        amount_line += 1
    amount_sym += 1

print(amount_line // h + 1 * (amount_line % h > 0))
