N, K = map(int, input().split())

backpack = [[0,0]]
for i in range(N):
  item = list(map(int, input().split()))
  backpack.append(item)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, K+1):
    if backpack[i][0] <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-backpack[i][0]]+backpack[i][1])
    else:
      dp[i][j] = dp[i-1][j]
    
print(dp[N][K])