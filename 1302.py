import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
books = [input().strip() for _ in range(n)]

cnt = Counter(books)
max_cnt = max(cnt.values())

# 가장 많이 팔린 것들 중 사전순으로 가장 앞선 제목
candidates = [title for title, c in cnt.items() if c == max_cnt]
print(min(candidates))