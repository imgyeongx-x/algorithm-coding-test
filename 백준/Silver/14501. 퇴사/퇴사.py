import sys
input = sys.stdin.readline

N = int(input())
li = [[0,0] for _ in range(N)]
dp = [0] * (N+1)

for i in range(N):
  li[i] = list(map(int, input().split()))

for i in range(N):
  t = li[i][0]
  p = li[i][1]

  if i + t <= N:
    for j in range(i+t, N+1):
      dp[j] = max(dp[j], p+dp[i])

print(max(dp))