from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []

def BFS_F(building, queue_f, visited_f):
  while queue_f:
    x, y = queue_f.popleft()
    for i in range(4):
      nx = x + dx[i] # 높이
      ny = y + dy[i] # 가로

      if 0 <= nx < h and 0 <= ny < w:
        if building[nx][ny] != '#' and visited_f[nx][ny] == 0:
          visited_f[nx][ny] = visited_f[x][y] + 1
          queue_f.append([nx, ny])


def BFS_S(building, queue_s, visited_s):
  while queue_s:
    x, y = queue_s.popleft()
    if x == 0 or x == h-1 or y == 0 or y == w-1:
      return visited_s[x][y]

    for i in range(4):
      nx = x + dx[i] # 높이
      ny = y + dy[i] # 가로

      if 0 <= nx < h and 0 <= ny < w:
        if building[nx][ny] == '.' and visited_s[nx][ny] == 0:
          if visited_f[nx][ny] > visited_s[x][y] + 1 or visited_f[nx][ny] == 0:
            visited_s[nx][ny] = visited_s[x][y] + 1
            queue_s.append([nx, ny])

  return "IMPOSSIBLE"

for _ in range(N):
  w, h = map(int, input().split())
  building = [list(input().strip()) for _ in range(h)]

  Spos = [0, 0]
  visited_f = [[0] * w for _ in range(h)]
  visited_s = [[0] * w for _ in range(h)]
  queue_f = deque()
  queue_s = deque()
  
  for i in range(h):
    for j in range(w):
      if building[i][j] == '@': # 상근 위치
        Spos = [i, j] # 높이, 가로
        visited_s[i][j] = 1
        queue_s.append([i, j])
      if building[i][j] == '*': # 불 위치
        visited_f[i][j] = 1
        queue_f.append([i, j])
  
  BFS_F(building, queue_f, visited_f)

  res.append(BFS_S(building, queue_s, visited_s))

for i in res:
  print(i)