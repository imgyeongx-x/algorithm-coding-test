import sys

input = sys.stdin.readline
N, M = map(int, input().split())
li = list(map(int, input().split()))

sum = []
tmp = 0

for i in range(0, N):
  sum.append(tmp + li[i])
  tmp += li[i]

for i in range(0, M):
  a, b = map(int, input().split())
  
  if a-2 < 0:
    aSum = 0
  else:
    aSum = sum[a-2]

  bSum = sum[b-1]
  print(bSum - aSum)
