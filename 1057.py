import sys
input = sys.stdin.readline

n, kim, lim = map(int, input().split())

round_cnt = 0
while kim != lim:
    kim = (kim + 1) // 2
    lim = (lim + 1) // 2
    round_cnt += 1

print(round_cnt)