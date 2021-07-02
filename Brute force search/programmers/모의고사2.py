def solution(answers):
    answer = []
    answerCount1 = 0
    answerCount2 = 0
    answerCount3 = 0

    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == supoja1[i % len(supoja1)]:
            answerCount1 += 1
        if answers[i] == supoja2[i % len(supoja2)]:
            answerCount2 += 1
        if answers[i] == supoja3[i % len(supoja3)]:
            answerCount3 += 1

    answerCount = [answerCount1, answerCount2, answerCount3]

    for supoja, score in enumerate(answerCount):
        if score == max(answerCount):
            answer.append(supoja + 1)

    return answer
