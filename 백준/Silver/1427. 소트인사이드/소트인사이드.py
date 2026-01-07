import sys
input = sys.stdin.readline

li = list(input())

for i in range(0, len(li) - 1):
  max = li[i]
  maxj = i
  for j in range(i+1, len(li) - 1):
    if max < li[j]:
      max = li[j]
      maxj = j
  if max != li[i]:
    tmp = li[maxj]
    li[maxj] = li[i]
    li[i] = tmp


for i in range(0, len(li)-1):
  print(li[i], end="")