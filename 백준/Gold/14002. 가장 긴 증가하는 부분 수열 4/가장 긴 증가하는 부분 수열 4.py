N = int(input())

li = list(map(int, input().split()))
dp = []
dp.append([li[0]])

for i in range(1, N):
  a = [li[i]]
  for j in range(0, i):
    if li[j] < li[i] and len(a) < len(dp[j]+[li[i]]):
      a = dp[j]+[li[i]]
  dp.append(a)

resN = 0
res = []
for i in range(N):
  if resN < len(dp[i]):
    resN = len(dp[i])
    res = dp[i]

print(resN)
for i in res:
  print(i, end=" ")