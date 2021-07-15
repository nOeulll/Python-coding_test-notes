data_input = input()
row = int(data_input[1])
clm = int(ord(data_input[0])) - int(ord('a')) + 1

cnt = 0

if row + 2 <= 8 and clm + 1 <= 8:
    cnt += 1
if row + 2 <= 8 and clm - 1 >= 1:
    cnt += 1
if row - 2 >= 1 and clm + 1 <= 8:
    cnt += 1
if row - 2 >= 1 and clm - 1 >= 1:
    cnt += 1
if clm + 2 <= 8 and row + 1 <= 8:
    cnt += 1
if clm + 2 <= 8 and row - 1 >= 1:
    cnt += 1
if clm - 2 >= 1 and row + 1 <= 8:
    cnt += 1
if clm - 2 >= 1 and row - 1 >= 1:
    cnt += 1

print(cnt)
