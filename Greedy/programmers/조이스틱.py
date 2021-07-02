def solution(name):
    # 1. 상하 조정하기
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    index = 0
    answer = 0

    while True:
        answer += change[index]
        change[index] = 0
        if sum(change) == 0:
            return answer

        # 2. 좌우 이동방향 정하기
        left, right = 1, 1
        while change[index - left] == 0:
            left += 1
        while change[index + right] == 0:
            right += 1

        # 3. index 이동 횟수 정하기 및 answer안에 갑 넣기
        index += -left if left < right else right
        answer += left if left < right else right
