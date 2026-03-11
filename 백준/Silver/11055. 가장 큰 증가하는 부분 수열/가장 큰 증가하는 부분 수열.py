N = int(input())

li = list(map(int, input().split()))
dp = [0] * N

dp[0] = li[0]

for i in range(1, N):
  for j in range(0, i):
    if li[j] < li[i]:
      if dp[j] + li[i] > dp[i]:
        dp[i] = dp[j] + li[i]
  if dp[i] == 0:
    dp[i] = li[i]

print(max(dp))