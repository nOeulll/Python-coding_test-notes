from itertools import combinations


def solution(clothes):
    data = dict()
    for i in clothes:
        if i[1] not in data:
            data[i[1]] = 1
        else:
            data[i[1]] += 1
    print(data)
    answer = 1
    items_list = list()
    for i in data.items():
        items_list.append(i[1])
    print(items_list)
    for i in items_list:
        answer *= (i+1)
    print(answer)
    return answer-1
