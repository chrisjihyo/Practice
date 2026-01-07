import sys
input = sys.stdin.readline

t = int(input())
answers = []

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    d2 = dx*dx + dy*dy

    if d2 == 0 and r1 == r2:
        answers.append("-1")
        continue

    sum_r = r1 + r2
    diff_r = r1 - r2

    sum2 = sum_r * sum_r
    diff2 = diff_r * diff_r

    if diff2 < d2 < sum2:
        answers.append("2")
    elif d2 == diff2 or d2 == sum2:
        answers.append("1")
    else:
        answers.append("0")

print("\n".join(answers))