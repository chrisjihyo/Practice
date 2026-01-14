import sys
input = sys.stdin.readline

n = int(input().strip())
nums = [input().strip() for _ in range(n)]

length = len(nums[0])

for k in range(1, length + 1):
    seen = set()
    for s in nums:
        seen.add(s[-k:])
    if len(seen) == n:
        print(k)
        break