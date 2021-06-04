n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[-1]  # 가장 큰 수
second = data[-2]  # 두 번재로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += int(m % (k + 1))

result = 0
result = count * first  # 가장 큰 수 더하기
result += (m-count) * first  # 두 번째로 큰 수 더하기

print(result)
