from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())
arr = [0] * N
sums = set()
ans = []

for i in range(N):
  arr[i] = int(input())

for i in arr:
  for j in arr:
    sums.add(i+j)

for i in arr:
  for j in arr:
    if (i-j) in sums:
      ans.append(i)

ans.sort()
print(ans[-1])