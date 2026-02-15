from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = []

def BFS(arr, x, y):
  queue = deque()
  queue.append([x,y])

  while queue:
    cur = queue.popleft()
    arr[cur[0]][cur[1]] = 0
    for i in range(4):
      nx = cur[0] + dx[i]
      ny = cur[1] + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 1:
          queue.append([nx, ny])
          arr[nx][ny] = 0
    
  

for i in range(N):
  M, N, K = map(int, input().split())
  # M = 가로
  # N = 세로

  arr = [[0] * M for _ in range(N)]
  queue = deque()
  cnt = 0

  for i in range(K):
    x, y = map(int, input().split())
    arr[y][x] = 1

  for a in range(N):
    for b in range(M):
      if arr[a][b] == 1:
        BFS(arr, a, b)
        cnt+=1

  res.append(cnt)

for i in res:
  print(i)