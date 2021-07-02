n, m = map(int, input().split())

result = 0

for i in range(n):
    card_line = list(map(int, input().split()))
    min_value = min(card_line)
    result = max(result, min_value)

print(result)
