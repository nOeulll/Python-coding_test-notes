import math


def solution(progresses, speeds):

    days = []
    for i in zip(progresses, speeds):
        days.append(math.ceil((100-i[0])/i[1]))

    time = days[0]

    for i in days:
        if i <= time:
            i = time
        else:
            time = i

    # days = [5, 10, 10, 10, 20, 20]
    tmp = days[0]
    count = 0
    answer = []

    for day in days:
        if tmp == day:
            count += 1
        else:
            answer.append(count)
            tmp = day
            count = 1
    answer.append(count)
    return answer
