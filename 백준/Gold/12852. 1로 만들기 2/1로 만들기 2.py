N = int(input())
dp = [[0]] * (N+1)
dp[1] = [1]
if N >= 2:
  dp[2] = [2, 1]
if N >= 3:
  dp[3] = [3, 1]

for i in range(4, N+1):
  dp[i] = [dp[i-1][0] + 1] + dp[i-1]
  if i % 2 == 0 and (len(dp[i]) > len(dp[i//2]) + 1):
    dp[i] = [dp[i//2][0] * 2] + dp[i//2]
  if i % 3 == 0 and len(dp[i]) > len(dp[i//3]) + 1:
    dp[i] = [dp[i//3][0] * 3] + dp[i//3]

print(len(dp[N])-1)
for i in dp[N]:
  print(i, end=" ")