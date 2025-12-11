import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0] * (N+1)]
sum = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N):
  a = [0] + list(map(int, input().split()))
  arr.append(a)

for i in range(1, N+1):
  for j in range(1, N+1):
    sum[i][j] = arr[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

for i in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  print(sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1])