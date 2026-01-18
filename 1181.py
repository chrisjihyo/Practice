import sys
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]

# 중복 제거 후 (길이, 사전순)으로 정렬
words = sorted(set(words), key=lambda w: (len(w), w))

print("\n".join(words))