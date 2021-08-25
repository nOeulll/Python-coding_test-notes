# 내가 푼 틀린 풀이

import copy


def solution(numbers):
    # numbers = [675, 10, 2]
    numbers_copy = copy.deepcopy(numbers)
    list = []
    cmp_list = []
    str_list = []

    for i in range(len(numbers_copy)):
        while(numbers_copy[i] != 0):
            list.append(numbers_copy[i] % 10)
            numbers_copy[i] = numbers_copy[i] // 10

        cmp_list.append(list[-1])

    for _ in range(len(cmp_list)):
        max_num = max(cmp_list)
        max_i = cmp_list.index(max_num)
        str_list.append(str(numbers[max_i]))
        cmp_list[max_i] = 0

    answer = ''.join(str_list)

    return answer
