import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# k = 변 길이 - 1 (좌표 차이)
for k in range(min(N, M) - 1, -1, -1):
    for i in range(N - k):
        for j in range(M - k):
            v = board[i][j]
            if v == board[i + k][j] and v == board[i][j + k] and v == board[i + k][j + k]:
                print((k + 1) * (k + 1))
                sys.exit(0)