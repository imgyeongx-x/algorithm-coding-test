import sys

input = sys.stdin.readline

N = int(input())
li = []

for i in range(N):
  li.append((int(input()), i))

Max = 0
sort_li = li.sort()

for i in range(N):
  if (Max < li[i][1] - i):
    Max = li[i][1] - i

print(Max + 1)