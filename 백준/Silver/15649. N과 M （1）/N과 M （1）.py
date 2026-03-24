from itertools import permutations

N, M = map(int, input().split())
li = []

for i in range(1, N+1):
  li.append(i)

for i in permutations(li, M):
  s = i
  for j in s:
    print(j, end=" ")
  print()