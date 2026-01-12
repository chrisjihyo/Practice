import sys
from bisect import bisect_left

input = sys.stdin.readline

L = int(input().strip())
S = sorted(map(int, input().split()))
n = int(input().strip())

# n이 집합 S 안에 있으면 좋은 구간 만들 수 없음
if n in S:
    print(0)
    sys.exit(0)

idx = bisect_left(S, n)

# n보다 바로 작은 수 a, 바로 큰 수 b 찾기
a = S[idx - 1] if idx > 0 else 0
b = S[idx] if idx < L else 1001  # 문제 범위가 1~1000이라면 상한은 1001로 두면 안전

# 가능한 (x, y): a < x <= n <= y < b, 그리고 x < y
ans = (n - a) * (b - n) - 1
print(ans)