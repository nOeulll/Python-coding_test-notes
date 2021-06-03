arr = input()
count = []


def solution():
    for i in arr:
        num = 0

        for i in arr:
            if(arr[0] == arr[i]):
                num += 1

        count.append(num)
