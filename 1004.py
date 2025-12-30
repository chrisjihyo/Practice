import sys
input = sys.stdin.readline

def is_inside(x, y, cx, cy, r):
    dx = x - cx
    dy = y - cy
    return dx*dx + dy*dy < r*r  # 경계는 포함하지 않음

t = int(input())
answers = []

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    a = 0  # 출발점 포함 행성 수
    b = 0  # 도착점 포함 행성 수
    c = 0  # 둘 다 포함 행성 수

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        inside1 = is_inside(x1, y1, cx, cy, r)
        inside2 = is_inside(x2, y2, cx, cy, r)

        if inside1:
            a += 1
        if inside2:
            b += 1
        if inside1 and inside2:
            c += 1

    answers.append(str(a + b - 2 * c))

print("\n".join(answers))
