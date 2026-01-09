import sys
input = sys.stdin.readline

A, B = input().split()
n, m = len(A), len(B)

best = 10**9

for start in range(m - n + 1):
    diff = 0
    for i in range(n):
        if A[i] != B[start + i]:
            diff += 1
    best = min(best, diff)

print(best)