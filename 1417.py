import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
dasom = int(input().strip())

others = []
for _ in range(n - 1):
    others.append(int(input().strip()))

# 후보가 1명이면 매수할 필요 없음
if n == 1:
    print(0)
    sys.exit(0)

# 최대 힙(파이썬은 최소 힙이라 음수로)
pq = [-x for x in others]
heapq.heapify(pq)

ans = 0
while pq and -pq[0] >= dasom:
    top = -heapq.heappop(pq)  # 가장 많은 표
    top -= 1
    dasom += 1
    ans += 1
    heapq.heappush(pq, -top)

print(ans)