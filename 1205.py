import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())

if n == 0:
    print(1)
    sys.exit(0)

scores = list(map(int, input().split()))

# 랭킹이 꽉 찼고, 새 점수가 최하위 점수 이하이면 진입 불가
if n == p and new_score <= scores[-1]:
    print(-1)
    sys.exit(0)

# 새 점수가 들어갈 순위(1-indexed) 계산: 나보다 큰 점수 개수 + 1
rank = 1
for s in scores:
    if s > new_score:
        rank += 1
    else:
        break

print(rank)