N, M = map(int, input().split())

li1, li2 = [], []

for i in range(N):
  li = list(map(int, input().split()))
  li1.append(li)

for i in range(N):
  li = list(map(int, input().split()))
  li2.append(li)

for i in range(N):
  for j in range(M):
    result = li1[i][j] + li2[i][j]
    print(result, end=" ")
  print()