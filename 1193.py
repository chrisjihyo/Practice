import sys
input = sys.stdin.readline

x = int(input().strip())

line = 1
while x > line:
    x -= line
    line += 1

# line번째 대각선에서 x번째 항
if line % 2 == 0:   # 짝수 대각선: 분자 증가, 분모 감소
    numerator = x
    denominator = line - x + 1
else:               # 홀수 대각선: 분자 감소, 분모 증가
    numerator = line - x + 1
    denominator = x

print(f"{numerator}/{denominator}")