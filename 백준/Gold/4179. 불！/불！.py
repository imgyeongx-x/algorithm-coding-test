from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
miro = [] 

Jqueue = deque()
Fqueue = deque()

visited_J = [[0] * C for _ in range(R)]
visited_F = [[0] * C for _ in range(R)]

for i in range(R):
  tmp = list(input())

  for j in range(len(tmp)):
    if tmp[j] == 'F':
      Fqueue.append([i, j])
      visited_F[i][j] = 1
    if tmp[j] == 'J':
      Jqueue.append([i, j])
      visited_J[i][j] = 1
  miro.append(tmp)

move = [
  [1, 0], 
  [-1, 0],
  [0, 1],
  [0, -1]
]

def BFS():
  while Fqueue:
    Fpos = Fqueue.popleft()

    for i in range(4):
      nx = Fpos[0] + move[i][0]
      ny = Fpos[1] + move[i][1]

      if 0<=nx<R and 0<=ny<C:
        if miro[nx][ny] != '#' and visited_F[nx][ny]==0:
          visited_F[nx][ny] = visited_F[Fpos[0]][Fpos[1]] + 1
          Fqueue.append([nx, ny])

  while Jqueue:
    Jpos = Jqueue.popleft()

    for i in range(4):
      nx = Jpos[0] + move[i][0]
      ny = Jpos[1] + move[i][1]

      if 0<=nx<R and 0<=ny<C:
        if miro[nx][ny] != '#' and visited_J[nx][ny] == 0: # 여기서 visited_J[nx][ny] == 0 안해서 메모리초과걸림
            if visited_F[nx][ny] > visited_J[Jpos[0]][Jpos[1]]+1 or visited_F[nx][ny]==0:
              visited_J[nx][ny] = visited_J[Jpos[0]][Jpos[1]]+1
              Jqueue.append([nx, ny])
      else:
        return visited_J[Jpos[0]][Jpos[1]]
      
  return "IMPOSSIBLE"

print(BFS());