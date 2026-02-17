N, M = map(int, input().split())
pwd = dict()

for _ in range(N):
  tmp = list(input().split(' '))
  pwd[tmp[0]] = tmp[1]

for _ in range(M):
  site = input()
  print(pwd[site])