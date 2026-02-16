from collections import deque

N = int(input())

move = [[-2, -1], [-1, -2],
        [-2, 1], [-1, 2],
        [2, -1], [1, -2],
        [2, 1], [1, 2]]

def BFS(L, arr, st_x, st_y, ed_x, ed_y):  
  queue = deque()
  if st_x == ed_x and st_y == ed_y:
    return 0

  queue.append([st_x, st_y])

  while queue:
    x, y = queue.popleft()
    for i in range(8):
      nx = x + move[i][0]
      ny = y + move[i][1]

      if 0 <= nx < L and 0 <= ny < L:
        if nx == ed_x and ny == ed_y:
          return arr[y][x]

        if arr[ny][nx] == 0:
          arr[ny][nx] = arr[y][x] + 1
          queue.append([nx, ny])
          
        # elif arr[ny][nx] > arr[y][x] + 1:
        #   arr[ny][nx] = arr[y][x] + 1
        #   queue.append([nx, ny])


res = []
for i in range(N):
  L = int(input())
  st_x, st_y = map(int, input().split())
  ed_x, ed_y = map(int, input().split())

  arr = [[0] * L for _ in range(L)]
  arr[st_y][st_x] = 1

  res.append(BFS(L, arr, st_x, st_y, ed_x, ed_y))

for i in res:
  print(i)