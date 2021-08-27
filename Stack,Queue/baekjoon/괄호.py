n = int(input())

for _ in range(n):
    test = input()
    test_ls = list(test)
    sum = 0

    for i in test_ls:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break

    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
