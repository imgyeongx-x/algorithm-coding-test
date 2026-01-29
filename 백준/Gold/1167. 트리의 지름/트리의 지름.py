from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]

for i in range(N):
  data = list(map(int, input().split()))
  index = 0
  S = data[index]
  index += 1
  while True:
    E = data[index]
    if E == -1:
      break
    V = data[index + 1]
    A[S].append((E,V))
    index += 2

distance = [0] * (N+1)
visited = [False] * (N+1)

def BFS(num):
  queue = deque()
  queue.append(num)
  visited[num] = True

  while (len(queue) != 0):
    data = queue.popleft()
    for i in A[data]:
      if not visited[i[0]]:
        visited[i[0]] = True
        queue.append(i[0])
        distance[i[0]] = distance[data] + i[1]

BFS(1)
Max = 1

for i in range(2, N+1):
  if distance[Max] < distance[i]:
    Max = i

distance = [0] * (N+1)
visited = [False] * (N+1)  
BFS(Max)
distance.sort()
print(distance[N])