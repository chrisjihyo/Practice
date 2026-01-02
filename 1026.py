import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 1. A는 오름차순 정렬
A.sort()

# 2. B에서 값이 큰 순서대로의 인덱스 구하기
b_indices = sorted(range(n), key=lambda i: B[i], reverse=True)

# 3. B가 큰 자리부터 A의 작은 값 배치
A_assigned = [0] * n
for i in range(n):
    A_assigned[b_indices[i]] = A[i]

# 4. 최소 합 계산
answer = 0
for i in range(n):
    answer += A_assigned[i] * B[i]

print(answer)