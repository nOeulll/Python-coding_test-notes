def solution(answers):

    answer = []
    supoja = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    solved = [0, 0, 0]

    for i in solved:
        num = 0
        for j in supoja:
            while True:
                for k in supoja[j]:
                    if k == answers[num]:
                        solved[i] += 1
                    num += 1
                if len(answers) - 1 == num:
                    return

    for person, score in enumerate(solved):
        if score == max(solved):
            answer.append(person + 1)

    return answer

answers = [1, 2, 3, 4, 5]
solution(answers)
