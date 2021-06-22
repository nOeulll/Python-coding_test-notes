def solution(progresses, speeds):
    answer = []
    finish = list(0 for i in range(len(progresses)))
    count = 0
    while True:
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]

                if progresses[i] == 100:
                    finish.append(1)
                else:
                    count += 1
    return answer
