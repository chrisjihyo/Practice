import sys
from math import comb

input = sys.stdin.readline

t = int(input())
answers = []

for _ in range(t):
    n, m = map(int, input().split())   # n = 서쪽, m = 동쪽
    answers.append(str(comb(m, n)))    # M C N

print("\n".join(answers))