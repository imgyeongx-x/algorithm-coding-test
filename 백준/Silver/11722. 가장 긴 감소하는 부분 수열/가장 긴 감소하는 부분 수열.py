N = int(input())

li = list(map(int, input().split()))
dp = [0] * N

dp[0] = 1
for i in range(1, N):
  for j in range(0, i):
    if li[j] > li[i]:
      if dp[j] + 1 > dp[i]:
        dp[i] = dp[j]+1
  if dp[i] == 0:
    dp[i] = 1

print(max(dp))