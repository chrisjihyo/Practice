import sys
input = sys.stdin.readline

s = input().strip()

# 연속된 0 덩어리 수, 1 덩어리 수 세기
count0 = 0
count1 = 0

prev = s[0]
if prev == '0':
    count0 += 1
else:
    count1 += 1

for ch in s[1:]:
    if ch != prev:
        if ch == '0':
            count0 += 1
        else:
            count1 += 1
        prev = ch

print(min(count0, count1))