import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
li = list(map(int, input().split()))
visited = [False] * N

cnt = 0

for i in range(1, N+1):
  comb = combinations(li, i)

  for c in comb:
    if sum(c) == S:
      cnt+=1

print(cnt)