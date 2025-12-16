import sys
input = sys.stdin.readline

N = int(input())
li = [0] * N

for i in range(N):
  li[i] = int(input())

for i in range(0, N-1):
  for j in range(0, N-i-1):
    if li[j] > li[j+1]:
      tmp = li[j]
      li[j] = li[j+1]
      li[j+1] = tmp

for i in range(N):
  print(li[i], end="\n")