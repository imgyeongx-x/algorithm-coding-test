import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
total = 0

def BFS():
  queue = deque()
  queue.append((0,0))
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      if (x + dx[i]) >= 0 and (x + dx[i]) < N and (y + dy[i]) >= 0 and (y + dy[i]) < M:
        if miro[x + dx[i]][y + dy[i]] == '1':
          queue.append((x+dx[i], y+dy[i]))
          miro[x+dx[i]][y+dy[i]] = int(miro[x][y])+1

miro = [[] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
  miro[i] = list(input())

BFS()

print(miro[N-1][M-1])