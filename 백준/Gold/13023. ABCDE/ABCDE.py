import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

li = [[] for _ in range(N)]
check = [False] * (N+1)
arrive = False

def DFS(num, depth):
  global arrive
  if depth == 5:
    arrive = True
    return
  check[num] = True
  for i in li[num]:
    if check[i] == False:
      DFS(i, depth+1)
  check[num] = False


for i in range(M):
  a, b = map(int, input().split(" "))
  li[a].append(b)
  li[b].append(a)

for i in range(N):
  DFS(i, 1)
  if arrive:
    break

if arrive:
  print(1)
else:
  print(0)