from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

move = [[-1, 0, 0],
        [1, 0, 0],
        [0, -1, 0],
        [0, 1, 0],
        [0, 0, -1],
        [0, 0, 1]]
queue = deque()

for i in range(H):
  for j in range(N):
    for k in range(M):
      if tomato[i][j][k] == 1:
        queue.append([i, j, k])
        visited[i][j][k] = 1
      if tomato[i][j][k] == -1:
        visited[i][j][k] = -1

while queue:
  z, y, x = queue.popleft()

  for i in range(6):
    nz = z + move[i][2]
    ny = y + move[i][1]
    nx = x + move[i][0]
    if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
      if tomato[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
        tomato[nz][ny][nx] = 1
        visited[nz][ny][nx] = visited[z][y][x] + 1
        queue.append([nz, ny, nx])
  
days = 0
res = 0
for i in range(H):
  for j in range(N):
    for k in range(M):
      if visited[i][j][k] == 0:
        res = -1
      if visited[i][j][k] > days:
        days = visited[i][j][k]

if res == -1:
  print(-1)
else:
  print(days - 1)