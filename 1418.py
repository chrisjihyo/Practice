import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def is_k_sejun(num, K):
    d = 2
    while d * d <= num:
        while num % d == 0:
            if d > K:
                return False
            num //= d
        d += 1
    # 마지막 남은 소인수
    if num > 1 and num > K:
        return False
    return True

count = 0
for i in range(1, N + 1):
    if is_k_sejun(i, K):
        count += 1

print(count)