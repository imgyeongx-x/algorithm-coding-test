import sys
input = sys.stdin.readline

from collections import deque

N, S = map(int, input().split())
arr = list(map(int, input().split()))

minArr = deque()

for i in range(N):
  while minArr and minArr[-1][0] > arr[i]:
    minArr.pop()
  minArr.append((arr[i], i))
  if minArr[0][1] <= i-S:
    minArr.popleft()
  print(minArr[0][0], end=" ")
