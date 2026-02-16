from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

painting = [['.']* N for _ in range(N)]

for i in range(N):
  tmp = list(input())
  painting[i] = tmp

v_normal = [[False] * N for _ in range(N)]
v_weak = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS_normal(painting, x, y):
  queue = deque()
  queue.append([x, y])
  v_normal[x][y] = True
  rgb = painting[x][y]

  while queue:
    posx, posy = queue.popleft()

    for i in range(4):
      nx = posx + dx[i]
      ny = posy + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if v_normal[nx][ny] == False and painting[nx][ny] == rgb:
          v_normal[nx][ny] = True
          queue.append([nx, ny])

def BFS_weak(painting, x, y):
  queue2 = deque()
  queue2.append([x, y])
  v_weak[x][y] = True
  rgb = painting[x][y]

  while queue2:
    posx, posy = queue2.popleft()

    for i in range(4):
      nx = posx + dx[i]
      ny = posy + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if v_weak[nx][ny] == False:
          if rgb == "R" or rgb == "G":
            if painting[nx][ny] == "R" or painting[nx][ny] == "G":
              v_weak[nx][ny] = True
              queue2.append([nx, ny])
          elif painting[nx][ny] == rgb:
            v_weak[nx][ny] = True
            queue2.append([nx, ny])

cnt_normal = 0
cnt_weak = 0

for i in range(N):
  for j in range(N):
    if v_normal[i][j] == False:
      BFS_normal(painting, i, j)
      cnt_normal += 1
    if v_weak[i][j] == False:
      BFS_weak(painting, i, j)
      cnt_weak += 1

print(cnt_normal, cnt_weak)