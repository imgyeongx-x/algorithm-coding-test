import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
from collections import deque

def BFS(paper, i, j):
  queue = deque()
  queue.append((i, j))
  paper[i][j] = 0
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  count = 0

  while queue:
    cur = queue.popleft()
    count +=1
    for i in range(4):
      nx, ny = cur[0] + dx[i], cur[1] + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if paper[nx][ny] == 1:
          queue.append((nx, ny))
          paper[nx][ny] = 0
  return count

n, m = map(int, input().split()) # n : 세로, m : 가로

paper = [[0 for _i in range(m)]] * n
cnt = 0
max = 0


for i in range(n):
  paper[i] = list(map(int, input().split()))

for i in range(n):
  for j in range(m):
    if paper[i][j] == 1:
      cnt += 1
      temp = BFS(paper,i, j)

      if temp > max:
        max = temp

print(cnt)
print(max)
