n = int(input())
m = list(input().split())

start = [1, 1]

for i in m:
    if i == 'L':
        if start[1] != 1:
            start[1] -= 1
    elif i == 'R':
        if start[1] != n:
            start[1] += 1
    elif i == 'U':
        if start[0] != 1:
            start[0] -= 1
    elif i == 'D':
        if start[0] != n:
            start[0] += 1

print(start[0], start[1])
