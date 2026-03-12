N = int(input())
li = list(map(int, input().split()))

l_dp = [0] * N
r_dp = [0] * N

for i in range(0, N):
  for j in range(0, i):
    if li[j] < li[i] and l_dp[j]+1 > l_dp[i]:
      l_dp[i] = l_dp[j]+1
  if l_dp[i] == 0:
    l_dp[i] = 1

for i in range(N-1, -1, -1):
  for j in range(N-1, i, -1):
    if li[j] < li[i] and r_dp[j]+1 > r_dp[i]:
      r_dp[i] = r_dp[j]+1
  if r_dp[i] == 0:
    r_dp[i] = 1

dp = [0] * N
for i in range(N):
  dp[i] = l_dp[i] + r_dp[i] - 1

print(max(dp))