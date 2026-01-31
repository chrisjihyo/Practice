import sys
input = sys.stdin.readline

n = input().strip()
digits = sorted(n, reverse=True)
print("".join(digits))