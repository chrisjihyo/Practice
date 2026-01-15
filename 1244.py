import sys
input = sys.stdin.readline

n = int(input().strip())
switches = [0] + list(map(int, input().split()))  # 1-indexed

m = int(input().strip())
for _ in range(m):
    gender, num = map(int, input().split())

    if gender == 1:  # 남학생: num의 배수 스위치 토글
        for i in range(num, n + 1, num):
            switches[i] ^= 1

    else:  # 여학생: num 기준 대칭 최대 구간 토글
        left = right = num
        while left - 1 >= 1 and right + 1 <= n and switches[left - 1] == switches[right + 1]:
            left -= 1
            right += 1
        for i in range(left, right + 1):
            switches[i] ^= 1

# 출력: 한 줄에 20개씩
for i in range(1, n + 1):
    print(switches[i], end=" ")
    if i % 20 == 0:
        print()
if n % 20 != 0:
    print()