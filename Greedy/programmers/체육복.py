def solution(n, lost, reserve):
    answer = 0

    for r in reserve[:]:
        if r in lost:
            reserve.remove(r)
            lost.remove(r)

    for l in lost[:]:
        if l+1 in reserve:
            reserve.remove(l+1)
            lost.remove(l)
        elif l-1 in reserve:
            reserve.remove(l-1)
            lost.remove(l)

    answer = n - len(lost)
    return answer
