import sys
input = sys.stdin.readline

x = int(input().strip())

cnt = 0
while x > 0:
    cnt += x & 1
    x >>= 1

print(cnt)