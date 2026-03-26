N = int(input())

li = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
  for j in range(0, i):
    if li[j] < li[i]:
      if dp[j] + 1 > dp[i]:
        dp[i] = dp[j] + 1

print(max(dp))