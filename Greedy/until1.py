# 1. 입력조건
# 첫째줄에 n(1 <= n <= 100,000)과 k(1 <= n <= 100,000)가 공백을 기준으로 하여 각각 자연수로 주어진다.

# 2. 출력조건
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.


# n, K를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += n - target
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
