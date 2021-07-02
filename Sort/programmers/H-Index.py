def solution(citations):
    citations.sort()
    for i in range(len(citations)+2):
        tmp = 0
        for j in citations:
            if j >= i:
                tmp += 1
        if i > tmp:
            return i-1
