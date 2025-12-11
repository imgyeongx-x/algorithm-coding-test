import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = [0] * n
num = 0
for i in range(n):
  s[i] = (arr[i] + num) % m
  num += arr[i]

ind = [0] * m
cnt = 0
for i in range(n):
  if (s[i] == 0):
    cnt+=1
  ind[s[i]]+=1

for i in range(m):
  if (ind[i]>1):
   cnt += (ind[i] * (ind[i]-1) // 2)

print(cnt)